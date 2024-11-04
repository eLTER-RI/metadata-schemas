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

export const PublishButton = ({record}) => {
    const [open, setOpen] = useState(false); // State to control modal visibility
    const [loading, setLoading] = useState(false); // State to control button loading state

    const draftId = _get(record, "id", "No-Id")

    const handlePublish = async () => {
        setLoading(true);
        try {
            const requestInfo = await axios.post(`/api/lter/${draftId}/draft/requests/publish_draft`)
            const publishRequestId = _get(requestInfo.data, "id", "No Link")
            await axios.post(`/api/requests/${publishRequestId}/actions/submit`)
            setOpen(false);
        } catch (error) {
            console.error("Error publishing:", error);
        } finally {
            setLoading(false);
            location.reload();
        }
    };

    const handlePublishButtonClick = (event) => {
        event.preventDefault();
        setOpen(true)
    }

    return (
        <div>
            <Button fluid secondary onClick={(e) => handlePublishButtonClick(e)}>Publish</Button>

            <Modal
                open={open}
                onClose={() => setOpen(false)}
                size="small"
            >
                <Modal.Header>Confirm Publish</Modal.Header>
                <Modal.Content>
                    <p>Are you sure you want to publish the draft ?</p>
                </Modal.Content>
                <Modal.Actions>
                    <Button onClick={() => setOpen(false)} disabled={loading}>
                        Cancel
                    </Button>
                    <Button
                        color="green"
                        onClick={() => handlePublish(draftId)}
                        loading={loading}
                        disabled={loading}
                    >
                        Confirm Publish
                    </Button>
                </Modal.Actions>
            </Modal>
        </div>
    );
};

// Define PropTypes
PublishButton.propTypes = {
    record: PropTypes.object.required,
};