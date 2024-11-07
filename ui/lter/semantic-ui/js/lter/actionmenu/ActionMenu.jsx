import React from 'react';
import PropTypes from "prop-types";
import _get from "lodash/get";
import {Button} from "semantic-ui-react";
import {DeleteButton} from "../../../templates/records_dashboard/search/components/DeleteButton";
import {EditButton} from "../../../templates/records_dashboard/search/components/EditButton";
import {ExternalWorkflowButton} from "../../../templates/records_dashboard/search/components/ExternalWorkflowButton";

export const ActionMenu = ({record}) => {
    const state = _get(record, 'state');

    return (
        <div>
            <DeleteButton record={record}/>
            <EditButton record={record} disabled={['running'].includes(state)}/>
            <ExternalWorkflowButton record={record} disabled={['running'].includes(state)}/>
        </div>
    );
};

ActionMenu.propTypes = {
    record: PropTypes.object.isRequired,
};