import React, {useContext, useState} from "react";
import PropTypes from "prop-types";
import Overridable from "react-overridable";

import _get from "lodash/get";

import {Grid, Item, Label, Icon, Button, Modal} from "semantic-ui-react";
import {withState, buildUID} from "react-searchkit";
import {SearchConfigurationContext} from "@js/invenio_search_ui/components";
import axios from "axios";


// import {i18next} from "@translations/i18next";


const stateIcons = {
    validated: {name: 'check circle', color: 'green'},
    error: {name: 'times circle', color: 'red'},
    queued: {name: 'question circle', color: 'blue'},
    draft: {name: 'question circle', color: 'blue'}
};

const ItemHeader = ({titles, state, viewLink}) => {

    const iconProps = stateIcons[state] || {};

    return (
        <Item.Header as="h2">
            {iconProps.name && <Icon {...iconProps} />}
            <a href={viewLink}>{titles[0].text}</a>
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

    const state = _get(result, "state")

    console.log(state)

    return (
        <Overridable
            id={buildUID("RecordsResultsListItem.layout", "", appName)}
            result={result}
            titles={titles}
            state={state}
            {...rest}
        >
            <Item data-testid="directions" key={result.id} className="search-listing-item"
                  href={result.links.self_html}>
                <Item.Content className="content">
                    <Grid>
                        <Grid.Row columns={2}>
                            <Grid.Column width={13} className="results-list item-main">
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
                                            {keyword.name}
                                        </Label>
                                    ))
                                ) : (
                                    <span>No keywords available</span>
                                )}
                            </Grid.Column>
                            <Grid.Column width={3}>
                                {state === 'validated' && <PublishButton record={result}/>}
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

const PublishButton = ({record}) => {
    const [open, setOpen] = useState(false); // State to control modal visibility
    const [loading, setLoading] = useState(false); // State to control button loading state

    const draftId = _get(record, "id", "No-Id")

    const handlePublish = async (id) => {
        setLoading(true);
        try {
            const requestInfo = await axios.post(`/api/lter/${draftId}/draft/requests/publish_draft`)
            const publishRequestId = _get(requestInfo.data, "id", "No Link")
            await axios.post(`/api/requests/${publishRequestId}/actions/submit`)
            setOpen(false);
        } catch (error) {
            console.error("Error publishing:", error);
        } finally {
            setLoading(false);
            location.reload();
        }
    };

    const handlePublishButtonClick = (event) => {
        event.preventDefault();
        setOpen(true)
    }

    return (
        <div>
            <Button secondary onClick={(e) => handlePublishButtonClick(e)}>Publish</Button>

            <Modal
                open={open}
                onClose={() => setOpen(false)}
                size="small"
            >
                <Modal.Header>Confirm Publish</Modal.Header>
                <Modal.Content>
                    <p>Are you sure you want to publish the draft ?</p>
                </Modal.Content>
                <Modal.Actions>
                    <Button onClick={() => setOpen(false)} disabled={loading}>
                        Cancel
                    </Button>
                    <Button
                        color="green"
                        onClick={() => handlePublish(draftId)}
                        loading={loading}
                        disabled={loading}
                    >
                        Confirm Publish
                    </Button>
                </Modal.Actions>
            </Modal>
        </div>
    );
};

// Define PropTypes
PublishButton.propTypes = {
    record: PropTypes.object,
};

export default ResultsListItemWithState;

