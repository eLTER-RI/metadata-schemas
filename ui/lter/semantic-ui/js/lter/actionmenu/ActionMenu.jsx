import React from 'react';
import PropTypes from "prop-types";
import {Grid, Label} from "semantic-ui-react";
import {DeleteButton} from "../../../templates/records_dashboard/search/components/DeleteButton";
import {EditButton} from "../../../templates/records_dashboard/search/components/EditButton";
import {ExternalWorkflowButton} from "../../../templates/records_dashboard/search/components/ExternalWorkflowButton";
import {PublishButton} from "../../../templates/records_dashboard/search/components/PublishButton";
import StateIcon from "../../../templates/components/StateIcon";

export const ActionMenu = ({draftId, state, isAdmin}) => {
    return (
        <Grid divided>
            <Grid.Row columns={3}>
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
            <Grid.Row>
                <Grid.Column>
                    <PublishButton draftId={draftId} disabled={state !== 'validated' && !isAdmin}/>
                </Grid.Column>
            </Grid.Row>
        </Grid>
    );
};

ActionMenu.propTypes = {
    draftId: PropTypes.string.isRequired,
    state: PropTypes.string.isRequired,
    isAdmin: PropTypes.bool
};