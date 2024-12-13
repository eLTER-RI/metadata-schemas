import React, {useContext} from "react";
import PropTypes from "prop-types";
import Overridable from "react-overridable";

import _get from "lodash/get";

import {Divider, Grid, Item, Label} from "semantic-ui-react";
import {withState, buildUID} from "react-searchkit";
import {SearchConfigurationContext} from "@js/invenio_search_ui/components";
import {ActionButton} from "./components/ActionButton";
import {PublishButton} from "./components/PublishButton";

import {useMediaQuery} from 'react-responsive';
import StateIcon from "../../components/StateIcon";


// import {i18next} from "@translations/i18next";


const ItemHeader = ({titles, state, viewLink}) => {

    let firstTitle = titles[0];
    const title = firstTitle.text ? firstTitle.text : "[NO TITLE - PLEASE FILL THE TITLE]";

    return (
        <Item.Header>
            <StateIcon state={state}/>
            <a href={viewLink}>{title}</a>
        </Item.Header>
    );
};

const ItemSubheader = ({description}) => {
    return (
        <>
            <Item.Meta>
                <Grid columns={1}>
                    <Grid.Column>
                        <Grid.Row className="ui double separated creatibutors">{description}</Grid.Row>
                    </Grid.Column>
                </Grid>
            </Item.Meta>
        </>
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
    const draftId = _get(result, "id", "error")
    const state = _get(result, "state")

    const isLargeScreen = useMediaQuery({minWidth: 2800});

    return (
        <Overridable
            id={buildUID("RecordsResultsListItem.layout", "", appName)}
            result={result}
            titles={titles}
            state={state}
            {...rest}
        >
            <Item data-testid="dashboardAssetListItem" key={result.id} className="search-listing-item">
                <Item.Content className="content">
                    <Grid>
                        <Grid.Row columns={3} className="computer only">
                            <Grid.Column width={isLargeScreen ? 13 : 12} className="results-list item-main">
                                <ItemHeader
                                    titles={titles}
                                    state={state}
                                    viewLink={result.links.self_html}
                                />
                                <ItemSubheader description={descriptions[0].description}/>
                                {keywords.length > 0 ? (
                                    keywords.map((keyword, index) => (
                                        <Label
                                            key={index}
                                            as="a"
                                            href={`?q=&f=metadata_keywords_name:${keyword.name}`}
                                            className="ui secondary"
                                            style={{margin: '5px'}}
                                        >
                                            {keyword.name === '' ? "empty keyword - fix/remove me" : keyword.name}
                                        </Label>
                                    ))
                                ) : (
                                    <span>No keywords available</span>
                                )}
                            </Grid.Column>
                            <Grid.Column width={2}>
                                {state === 'validated' && <PublishButton draftId={draftId}/>}
                            </Grid.Column>
                            <Grid.Column width={isLargeScreen ? 1 : 2}>
                                {!['published'].includes(state) && <ActionButton record={result}/>}
                            </Grid.Column>
                        </Grid.Row>
                        <Grid.Row className="tablet mobile only">
                            <Grid.Column width={12} className="results-list item-main">
                                <ItemHeader
                                    titles={titles}
                                    state={state}
                                    viewLink={result.links.self_html}
                                />
                                <Divider/>
                                <Grid>
                                    <Grid.Row columns={2}>
                                        {
                                            state === 'validated' && <Grid.Column>
                                                <PublishButton draftId={draftId}/>
                                            </Grid.Column>
                                        }
                                        <Grid.Column>
                                            {!['published'].includes(state) && <ActionButton record={result}/>}
                                        </Grid.Column>
                                    </Grid.Row>
                                </Grid>
                                <Divider/>
                                <ItemSubheader description={descriptions[0].description}/>
                                {keywords.length > 0 ? (
                                    keywords.map((keyword, index) => (
                                        <Label
                                            key={index}
                                            as="a"
                                            href={`?q=&f=metadata_keywords_name:${keyword.name}`}
                                            className="ui secondary"
                                            style={{margin: '5px'}}
                                        >
                                            {keyword.name}
                                        </Label>
                                    ))
                                ) : (
                                    <span>No keywords available</span>
                                )}
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

