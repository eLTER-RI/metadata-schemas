import React from 'react';
import PropTypes from "prop-types";
import {Grid} from "semantic-ui-react";
import {DeleteButton} from "../../../templates/records_dashboard/search/components/DeleteButton";
import {EditButton} from "../../../templates/records_dashboard/search/components/EditButton";
import {ExternalWorkflowButton} from "../../../templates/records_dashboard/search/components/ExternalWorkflowButton";

export const ActionMenu = ({draftId, state}) => {
    return (
        <Grid columns={3} divided>
            <Grid.Row>
                <Grid.Column>
                    <DeleteButton draftId={draftId}/>
                </Grid.Column>
                <Grid.Column>
                    <EditButton draftId={draftId} disabled={['running'].includes(state)}/>
                </Grid.Column>
                <Grid.Column>
                    <ExternalWorkflowButton draftId={draftId} disabled={['running'].includes(state)}/>
                </Grid.Column>
            </Grid.Row>
        </Grid>
    );
};

ActionMenu.propTypes = {
    draftId: PropTypes.string.isRequired,
    state: PropTypes.string.isRequired,
};