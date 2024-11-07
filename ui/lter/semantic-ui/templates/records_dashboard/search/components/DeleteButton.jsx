import React, { useState } from 'react';
import PropTypes from "prop-types";
import { Button, Modal } from "semantic-ui-react";
import {useDeleteDraft} from "../../../hooks";
import {useNavigation} from "../../../tools";

export const DeleteButton = ({ draftId }) => {
    const [open, setOpen] = useState(false);
    const { deleteDraft, loading } = useDeleteDraft(draftId);
    const navigate = useNavigation()

    const handleDelete = async () => {
        await deleteDraft();
        setOpen(false);
    };

    return (
        <>
            <Button fluid negative onClick={() => setOpen(true)}>Delete</Button>

            <Modal open={open} onClose={() => setOpen(false)} size="small">
                <Modal.Header>Confirm Delete</Modal.Header>
                <Modal.Content>
                    <p>Are you sure you want to delete this draft? This action cannot be undone.</p>
                </Modal.Content>
                <Modal.Actions>
                    <Button onClick={() => setOpen(false)} disabled={loading}>Cancel</Button>
                    <Button color="red" onClick={handleDelete} loading={loading} disabled={loading}>Confirm Delete</Button>
                </Modal.Actions>
            </Modal>
        </>
    );
};

DeleteButton.propTypes = {
    draftId: PropTypes.string.isRequired,
};
