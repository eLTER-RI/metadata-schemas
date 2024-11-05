import React from 'react';
import PropTypes from "prop-types";
import { Button } from "semantic-ui-react";
import _get from "lodash/get";

export const EditButton = ({ record }) => {
    const editUrl = _get(record, 'links.edit_html', 'Error');
    return (
        <Button color="orange" fluid href={editUrl}>
            Edit
        </Button>
    );
};

EditButton.propTypes = {
    record: PropTypes.object.isRequired,
};
