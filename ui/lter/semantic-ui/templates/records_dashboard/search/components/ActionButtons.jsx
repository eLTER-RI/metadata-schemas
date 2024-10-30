import React, {useState} from 'react';
import PropTypes from "prop-types";
import _get from "lodash/get";
import axios from "axios";
import {Button, Modal} from "semantic-ui-react";

export const DeleteButton = ({record}) => {
    const [open, setOpen] = useState(false);
    const [loading, setLoading] = useState(false);

    const draftId = _get(record, "id", "No-Id");

    const handleDelete = async (id) => {
        setLoading(true);
        try {
            await axios.delete(`/api/lter/${draftId}/draft`);
            setOpen(false);
        } catch (error) {
            console.error("Error deleting:", error);
        } finally {
            setLoading(false);
            location.reload();
        }
    };

    const handleDeleteButtonClick = (event) => {
        event.preventDefault();
        setOpen(true);
    };

    return (
        <div>
            <Button fluid negative onClick={(e) => handleDeleteButtonClick(e)}>Delete</Button>

            <Modal
                open={open}
                onClose={() => setOpen(false)}
                size="small"
            >
                <Modal.Header>Confirm Delete</Modal.Header>
                <Modal.Content>
                    <p>Are you sure you want to delete this draft? This action cannot be undone.</p>
                </Modal.Content>
                <Modal.Actions>
                    <Button onClick={() => setOpen(false)} disabled={loading}>
                        Cancel
                    </Button>
                    <Button
                        color="red"
                        onClick={() => handleDelete(draftId)}
                        loading={loading}
                        disabled={loading}
                    >
                        Confirm Delete
                    </Button>
                </Modal.Actions>
            </Modal>
        </div>
    );
};

DeleteButton.propTypes = {
    record: PropTypes.object.required,
};