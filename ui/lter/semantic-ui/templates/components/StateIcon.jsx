import React from 'react';
import {Icon, Loader, Popup} from "semantic-ui-react";
import PropTypes from "prop-types";

const stateIcons = {
    validated: {name: 'check circle', color: 'green'},
    error: {name: 'times circle', color: 'red'},
    draft: {name: 'question circle', color: 'blue'},
    published: {name: 'globe', color: 'blue'}
};

export default function StateIcon({ state }) {
    const iconProps = stateIcons[state] || {};
    return (
        <Popup content={state} trigger={
            state === 'running' ? (
                <Loader active inline size="mini" indeterminate/>
            ) : (
                iconProps.name && <Icon {...iconProps} aria-label={state}/>
            )
        }/>
    )
}

StateIcon.defaultProps = {
    state: PropTypes.string.isRequired,
};