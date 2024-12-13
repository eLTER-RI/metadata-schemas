import React, {useContext} from "react";
import PropTypes from "prop-types";
import Overridable from "react-overridable";

import _get from "lodash/get";

import {Button, Grid, Header, Item, Label} from "semantic-ui-react";
import {withState, buildUID} from "react-searchkit";
import {SearchConfigurationContext} from "@js/invenio_search_ui/components";

import {i18next} from "@translations/i18next";

const ItemHeader = ({titles, viewLink}) => {
    return (
        <Header className="oxfordBlue" as="h2" href={viewLink}>{titles[0].text}</Header>
    );
};

const ItemSubheader = ({description}) => {
    return (
        <Item.Meta>
            <Grid columns={1}>
                <Grid.Column>
                    <Grid.Row className="ui double separated creatibutors">{description}</Grid.Row>
                </Grid.Column>
            </Grid>
        </Item.Meta>
    );
};

export const ResultsListItemComponent = ({
                                             currentQueryState,
                                             result,
                                             appName,
                                             ...rest
                                         }) => {
    const searchAppConfig = useContext(SearchConfigurationContext);

    const titles = _get(result, "metadata.titles", [{"text": "No Title"}]);
    const descriptions = _get(result, "metadata.descriptions", [{"description": "No Description"}])
    const keywords = _get(result, "metadata.keywords", [])

    const getKeywords = () => {
        return keywords.length > 0 ? (
            keywords.map((keyword, index) => (
                keyword.name === '' ?
                    <Button className="disabled" size="small">Empty keyword</Button> :
                    <Button
                        key={index}
                        size="small"
                        as="a"
                        href={`?q=&f=metadata_keywords_name:${keyword.name}`}
                        className="ui secondary"
                        style={{margin: '2px'}}
                    >
                        {keyword.name}
                    </Button>
            ))
        ) : (
            <span>No keywords available</span>
        );
    }

    return (
        <Overridable
            id={buildUID("RecordsResultsListItem.layout", "", appName)}
            result={result}
            titles={titles}
            {...rest}
        >
            <Item key={result.id} className="search-listing-item" href={result.links.self_html}>
                <Item.Content className="content">
                    <Grid>
                        <Grid.Row columns={1}>
                            <Grid.Column className="results-list item-main">
                                <ItemHeader
                                    titles={titles}
                                    viewLink={result.links.self_html}
                                />
                                <ItemSubheader description={descriptions[0].description}/>
                                <Item.Extra>
                                    {getKeywords()}
                                </Item.Extra>
                            </Grid.Column>
                        </Grid.Row>
                    </Grid>
                </Item.Content>
            </Item>
        </Overridable>
    );
};

ResultsListItemComponent.propTypes = {
    currentQueryState: PropTypes.object,
    result: PropTypes.object.isRequired,
    appName: PropTypes.string,
};

ResultsListItemComponent.defaultProps = {
    currentQueryState: null,
    appName: "",
};

export const ResultsListItem = (props) => {
    return (
        <Overridable id={buildUID("ResultsListItem", "", props.appName)} {...props}>
            <ResultsListItemComponent {...props} />
        </Overridable>
    );
};

ResultsListItem.propTypes = {
    currentQueryState: PropTypes.object,
    result: PropTypes.object.isRequired,
    appName: PropTypes.string,
};

ResultsListItem.defaultProps = {
    currentQueryState: null,
    appName: "",
};

export const ResultsListItemWithState = withState(
    ({currentQueryState, updateQueryState, result, appName}) => (
        <ResultsListItem
            currentQueryState={currentQueryState}
            updateQueryState={updateQueryState}
            result={result}
            appName={appName}
        />
    )
);

ResultsListItemWithState.propTypes = {
    currentQueryState: PropTypes.object,
    result: PropTypes.object.isRequired,
};

ResultsListItemWithState.defaultProps = {
    currentQueryState: null,
};

export default ResultsListItemWithState;
