import React, {useState} from 'react';
import PropTypes from "prop-types";
import {Button, Modal, Popup} from "semantic-ui-react";
import {usePublishDraft} from "../../../hooks";

export const PublishButton = ({draftId, disabled}) => {
    const [open, setOpen] = useState(false);
    const {publishDraft, loading} = usePublishDraft(draftId);

    const handlePublish = async () => {
        await publishDraft();
        setOpen(false);
        location.reload();
    };

    return (
        <>
            <Button fluid secondary disabled={disabled ?? false} onClick={() => setOpen(true)}>Publish</Button>

            <Modal open={open} onClose={() => setOpen(false)} size="small">
                <Modal.Header>Confirm Publish</Modal.Header>
                <Modal.Content>
                    <p>Are you sure you want to publish the draft?</p>
                </Modal.Content>
                <Modal.Actions>
                    <Button onClick={() => setOpen(false)} disabled={loading}>Cancel</Button>
                    <Button color="green" onClick={handlePublish} loading={loading} disabled={loading}>Confirm
                        Publish</Button>
                </Modal.Actions>
            </Modal>
        </>
    );
};

PublishButton.propTypes = {
    draftId: PropTypes.string.isRequired,
    disabled: PropTypes.boolean
};
