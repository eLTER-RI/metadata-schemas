import logging
import pdb
from datetime import datetime
import random
import string

from invenio_records_resources.services.uow import RecordCommitOp

from oarepo_requests.types.generic import (
    OARepoAcceptAction,
    OARepoSubmitAction,
    OARepoDeclineAction
)

import requests

from flask import current_app

logger = logging.getLogger(__name__)

def generate_random_string(size):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(size))


def get_ingest_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {current_app.config['INGEST_API_KEY']}'
    }

class ExternalWorkflowHistoryMixin:
    def add_to_history(self, topic, workflowHandle, workflowTemplateId, status, uow):
        topic['externalWorkflow'].setdefault('history', []).append(
            {
                "workflowHandle": workflowHandle,
                "workflowTemplateId": workflowTemplateId,
                "date": datetime.now().isoformat(),
                "status": status,
            }
        )

        uow.register(RecordCommitOp(topic))

    @staticmethod
    def get_workflow_id(topic):
        return topic['externalWorkflow']['history'][-1]['workflowHandle']

    @staticmethod
    def get_workflow_type_id(topic):
        return topic['externalWorkflow']['history'][-1]['workflowTemplateId']


class ExternalWorkflowSubmitAction(ExternalWorkflowHistoryMixin, OARepoSubmitAction):
    def apply(self, identity, request_type, topic, uow, *args, **kwargs):
        data = {
            "draftId": topic['id'],
            "requestId": str(self.request.id)
        }
        headers = get_ingest_headers()
        hostname = current_app.config['INGEST_API_HOSTNAME']

        dev = current_app.config['DEV']
        workflow_type_id = topic['externalWorkflow']['defaultWorkflowTemplateId']

        if not dev:
            workflow_type_id = topic['externalWorkflow']['defaultWorkflowTemplateId']
            response = requests.post(f"{hostname}/api/v1/ingest/batch/simple/{workflow_type_id}", json=data, headers=headers)
            response.raise_for_status()
            data = response.json()
            workflow_template_id = data.get('batchWorkflowHandle', 'Error')
            self.add_to_history(topic, workflow_template_id, workflow_type_id, 'Running', uow)
            return response
        else:
            self.add_to_history(topic, generate_random_string(10), workflow_type_id, 'Running', uow)

class ExternalWorkflowDeclineAction(ExternalWorkflowHistoryMixin, OARepoDeclineAction):
    def apply(self, identity, request_type, topic, uow, *args, **kwargs):
        self.add_to_history(topic, self.get_workflow_id(topic), self.get_workflow_type_id(topic), 'Declined', uow)
        print(f"External workflow was declined")

class ExternalWorkflowAcceptAction(ExternalWorkflowHistoryMixin, OARepoAcceptAction):
    def apply(self, identity, request_type, topic, uow, *args, **kwargs):
        self.add_to_history(topic, self.get_workflow_id(topic), self.get_workflow_type_id(topic), 'Accepted', uow)
        print(f"External workflow finished successfully")
