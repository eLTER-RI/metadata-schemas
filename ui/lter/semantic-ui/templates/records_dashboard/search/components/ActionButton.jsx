import React from 'react';
import PropTypes from "prop-types";
import _get from "lodash/get";
import {Dropdown} from "semantic-ui-react";
import {DeleteButton} from "./DeleteButton";
import {EditButton} from "./EditButton";
import {ExternalWorkflowButton} from "./ExternalWorkflowButton";

export const ActionButton = ({record}) => {

    const state = _get(record, 'state')
    const draftId = _get(record, 'id')

    return (
        <Dropdown
            text={'Actions'}
            icon="list"
            floating
            labeled
            button
            className='icon'
        >
            <Dropdown.Menu>
                <Dropdown.Item>
                    <DeleteButton draftId={draftId}/>
                </Dropdown.Item>
                <Dropdown.Item disabled={['running'].includes(state)}>
                    <EditButton draftId={draftId}/>
                </Dropdown.Item>
                <Dropdown.Item disabled={['running'].includes(state)}>
                    <ExternalWorkflowButton draftId={draftId}/>
                </Dropdown.Item>
            </Dropdown.Menu>
        </Dropdown>
    );
};

ActionButton.propTypes = {
    record: PropTypes.object.isRequired,
};
