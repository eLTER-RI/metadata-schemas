import React from 'react';
import {Icon, Loader, Popup} from "semantic-ui-react";
import {ResultsListItem} from "../records_dashboard/search/ResultsListItem";
import PropTypes from "prop-types";

const stateIcons = {
    validated: {name: 'check circle', color: 'green'},
    error: {name: 'times circle', color: 'red'},
    draft: {name: 'question circle', color: 'blue'},
    published: {name: 'globe', color: 'blue'}
};

export default function StateIcon({ state, disabledPopup }) {
    const iconProps = stateIcons[state] || {};

    return (
        <Popup disabled={disabledPopup ?? false} content={state} trigger={
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
    disabledPopup: PropTypes.bool
};