import React from 'react';
import PropTypes from "prop-types";
import { Button } from "semantic-ui-react";

export const EditButton = ({ draftId, disabled }) => {
    const editUrl = `/lter/${draftId}/edit`
    return (
        <Button color="orange" fluid href={editUrl} disabled={disabled ?? false}>
            Edit
        </Button>
    );
};

EditButton.propTypes = {
    draftId: PropTypes.string.isRequired,
    disabled: PropTypes.boolean
};
