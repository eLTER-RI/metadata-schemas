import {useState} from 'react';
import axios from 'axios';

// Not used - probably in the future ?
export const useCreateDraft = () => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [response, setResponse] = useState(null)

    const createDraft = async (metadata) => {
        setLoading(true);
        setError(null);
        try {
            let data = {
                "files": {
                    "enabled": true
                },
                "parent": {
                    "communities": {
                        "default": "elter"
                    }
                },
                "metadata": {}
            }
            if (metadata) {
                data = metadata
            }
            const res = await axios.post("/api/lter", data, {
                headers: {
                    "Content-Type": 'application/json'
                }
            })
            setResponse(response.data)
        } catch (err) {
            setError(err)
            console.log(err)
        } finally {
            setLoading(false);
        }
    }
}

export const useDeleteDraft = (draftId) => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const deleteDraft = async () => {
        setLoading(true);
        setError(null);
        try {
            await axios.delete(`/api/lter/${draftId}/draft`);
        } catch (err) {
            console.error("Error deleting draft:", err);
            setError(err);
        } finally {
            setLoading(false);
        }
    };

    return {deleteDraft, loading, error};
};

export const usePublishDraft = (draftId) => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const publishDraft = async () => {
        setLoading(true);
        setError(null);
        try {
            const requestInfo = await axios.post(`/api/lter/${draftId}/draft/requests/publish_draft`);
            const publishRequestId = requestInfo.data.id;
            await axios.post(`/api/requests/${publishRequestId}/actions/submit`);
        } catch (err) {
            console.error("Error publishing draft:", err);
            setError(err);
        } finally {
            setLoading(false);
        }
    };

    return {publishDraft, loading, error};
};

export const useRunExternalWorkflow = (draftId) => {
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const runExternalWorkflow = async () => {
        setLoading(true);
        setError(null);
        try {
            const requestInfo = await axios.post(`/api/lter/${draftId}/draft/requests/run_external_workflow`);
            const requestId = requestInfo.data.id;
            await axios.post(`/api/requests/${requestId}/actions/submit`);
        } catch (err) {
            console.error("Error running external workflow:", err);
            setError(err);
        } finally {
            setLoading(false);
        }
    };

    return {runExternalWorkflow, loading, error};
};
