import React, { useState } from 'react';
import PropTypes from "prop-types";
import { Button, Modal } from "semantic-ui-react";
import {useRunExternalWorkflow} from "../../../hooks";

export const ExternalWorkflowButton = ({ draftId, disabled }) => {
    const [open, setOpen] = useState(false);
    const { runExternalWorkflow, loading } = useRunExternalWorkflow(draftId);

    const handleRun = async () => {
        await runExternalWorkflow();
        setOpen(false);
        location.reload();
    };

    return (
        <>
            <Button fluid secondary onClick={() => setOpen(true)} disabled={disabled ?? false}>Run workflow</Button>

            <Modal open={open} onClose={() => setOpen(false)} size="small">
                <Modal.Header>Confirm Run External Workflow</Modal.Header>
                <Modal.Content>
                    <p>Are you sure you want to run external checks on this draft?</p>
                </Modal.Content>
                <Modal.Actions>
                    <Button onClick={() => setOpen(false)} disabled={loading}>Cancel</Button>
                    <Button color="green" onClick={handleRun} loading={loading} disabled={loading}>Confirm</Button>
                </Modal.Actions>
            </Modal>
        </>
    );
};

ExternalWorkflowButton.propTypes = {
    draftId: PropTypes.string.isRequired,
    disabled: PropTypes.boolean
};
