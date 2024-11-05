import React, { useState } from 'react';
import PropTypes from "prop-types";
import { Button, Modal } from "semantic-ui-react";
import _get from "lodash/get";
import {usePublishDraft} from "../../../hooks";

export const PublishButton = ({ record }) => {
    const [open, setOpen] = useState(false);
    const draftId = _get(record, "id", "No-Id");
    const { publishDraft, loading } = usePublishDraft(draftId);

    const handlePublish = async () => {
        await publishDraft();
        setOpen(false);
        location.reload();
    };

    return (
        <>
            <Button fluid secondary onClick={() => setOpen(true)}>Publish</Button>

            <Modal open={open} onClose={() => setOpen(false)} size="small">
                <Modal.Header>Confirm Publish</Modal.Header>
                <Modal.Content>
                    <p>Are you sure you want to publish the draft?</p>
                </Modal.Content>
                <Modal.Actions>
                    <Button onClick={() => setOpen(false)} disabled={loading}>Cancel</Button>
                    <Button color="green" onClick={handlePublish} loading={loading} disabled={loading}>Confirm Publish</Button>
                </Modal.Actions>
            </Modal>
        </>
    );
};

PublishButton.propTypes = {
    record: PropTypes.object.isRequired,
};
