import React, { useState } from 'react';
import { Button, Modal } from "semantic-ui-react";

export const CreateAssetButton = () => {
    const [open, setOpen] = useState(false);

    const handleCreateButtonClick = () => {
        setOpen(false);
    };

    const handleButtonClick = (event) => {
        event.preventDefault();
        setOpen(true);
    };

    return (
        <>
            <Button fluid secondary onClick={handleButtonClick}>Create Asset</Button>

            <Modal
                open={open}
                onClose={() => setOpen(false)}
                size="small"
            >
                <Modal.Header>Confirm Creating a New Draft Record</Modal.Header>
                <Modal.Content>
                    <p>This action will create a new draft record. Do you want to continue?</p>
                </Modal.Content>
                <Modal.Actions>
                    <Button onClick={() => setOpen(false)}>Cancel</Button>
                    <Button
                        color="green"
                        href={'/lter/_new'}
                        onClick={handleCreateButtonClick}
                    >
                        Confirm Create
                    </Button>
                </Modal.Actions>
            </Modal>
        </>
    );
};
