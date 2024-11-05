import React from 'react';
import PropTypes from "prop-types";
import _get from "lodash/get";
import {Dropdown} from "semantic-ui-react";
import {DeleteButton} from "./DeleteButton";
import {EditButton} from "./EditButton";
import {ExternalWorkflowButton} from "./ExternalWorkflowButton";

export const ActionButton = ({record}) => {

    const state = _get(record, 'state')

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
                    <DeleteButton record={record}/>
                </Dropdown.Item>
                <Dropdown.Item disabled={['running'].includes(state)}>
                    <EditButton record={record}/>
                </Dropdown.Item>
                <Dropdown.Item disabled={['running'].includes(state)}>
                    <ExternalWorkflowButton record={record}/>
                </Dropdown.Item>
            </Dropdown.Menu>
        </Dropdown>
    );
};

ActionButton.propTypes = {
    record: PropTypes.object.isRequired,
};
