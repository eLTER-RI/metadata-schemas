import React, {useState} from 'react';
import PropTypes from "prop-types";
import _get from "lodash/get";
import axios from "axios";
import {Dropdown, Button, Modal} from "semantic-ui-react";

export const ActionButton = ({record}) => {

    const state = _get(record, 'state')

    return (
        <Dropdown
            fluid
            text={'Action Menu'}
            icon="caret down"
            floating
            labeled
            button
            className='icon'
        >
            <Dropdown.Menu>
                <Dropdown.Item>
                    <DeleteButton record={record}/>
                </Dropdown.Item>
                <Dropdown.Item disabled={['running'].includes(state)}>
                    <EditButton record={record}/>
                </Dropdown.Item>
                <Dropdown.Item disabled={['running'].includes(state)}>
                    <ExternalWorkflowButton record={record}/>
                </Dropdown.Item>
            </Dropdown.Menu>
        </Dropdown>
    );
};

ActionButton.propTypes = {
    record: PropTypes.object.isRequired,
};

export const DeleteButton = ({record}) => {
    const [open, setOpen] = useState(false);
    const [loading, setLoading] = useState(false);

    const draftId = _get(record, "id", "No-Id");

    const handleDelete = async () => {
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
        <>
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
        </>
    );
};

DeleteButton.propTypes = {
    record: PropTypes.object.required,
};

export const PublishButton = ({record}) => {
    const [open, setOpen] = useState(false);
    const [loading, setLoading] = useState(false);

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
        <>
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
        </>
    );
};

PublishButton.propTypes = {
    record: PropTypes.object.required,
};

export const EditButton = ({record}) => {
    const editUrl = _get(record, 'links.edit_html', 'Error')
    return (
        <Button color="orange" fluid href={editUrl}>
            Edit
        </Button>
    );
}

EditButton.propTypes = {
    record: PropTypes.object.required,
};

export const ExternalWorkflowButton = ({record}) => {


    const [open, setOpen] = useState(false);
    const [loading, setLoading] = useState(false);

    const draftId = _get(record, 'id', "No_Id")
    const state = _get(record, 'state')

    const handleRunExternalWorkflow = async () => {
        setLoading(true);
        try {
            const requestInfo = await axios.post(`/api/lter/${draftId}/draft/requests/run_external_workflow`);
            const requestId = _get(requestInfo.data, "id", "No Link")
            await axios.post(`/api/requests/${requestId}/actions/submit`)
            setOpen(false);
        } catch (error) {
            console.error("Error running external workflow:", error);
        } finally {
            setLoading(false);
            location.reload();
        }
    }

    const handleButtonClick = (event) => {
        event.preventDefault();
        setOpen(true)
    }

    return (
        <>
            <Button fluid secondary onClick={(e) => {
                state === 'validated' ? handleButtonClick(e) : handleRunExternalWorkflow()
            }}>Run workflow</Button>

            <Modal
                open={open}
                onClose={() => setOpen(false)}
                size="small"
            >
                <Modal.Header>Confirm Run External Workflow</Modal.Header>
                <Modal.Content>
                    <p>Are you sure you want to run external checks when the draft is validated?</p>
                </Modal.Content>
                <Modal.Actions>
                    <Button onClick={() => setOpen(false)} disabled={loading}>
                        Cancel
                    </Button>
                    <Button
                        color="green"
                        onClick={() => handleRunExternalWorkflow(draftId)}
                        loading={loading}
                        disabled={loading}
                    >
                        Confirm
                    </Button>
                </Modal.Actions>
            </Modal>
        </>
    )
}

export const CreateAssetButton = () => {
    const [open, setOpen] = useState(false);

    const handleCreateButtonClick = async () => {
        setOpen(false);
    }

    const handleButtonClick = (event) => {
        event.preventDefault();
        setOpen(true);
    }

    return (
        <>
            <Button fluid secondary onClick={handleButtonClick}>Create asset</Button>

            <Modal
                open={open}
                onClose={() => setOpen(false)}
                size="small"
            >
                <Modal.Header>Confirm creating a new draft record</Modal.Header>
                <Modal.Content>
                    <p>This action will create a new draft record. Do you want to continue?</p>
                </Modal.Content>
                <Modal.Actions>
                    <Button onClick={() => setOpen(false)}>
                        Cancel
                    </Button>
                    <Button
                        color="green"
                        href={'/lter/_new'}
                        onClick={() => handleCreateButtonClick()}
                    >
                        Confirm create
                    </Button>
                </Modal.Actions>
            </Modal>
        </>
    )
}