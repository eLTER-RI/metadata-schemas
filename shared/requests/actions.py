import logging
import pdb

from oarepo_requests.types.generic import (
    OARepoAcceptAction,
    OARepoSubmitAction,
    OARepoDeclineAction
)

import requests

from flask import current_app

logger = logging.getLogger(__name__)


def get_ingest_headers():
    return {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {current_app.config['INGEST_API_KEY']}'
    }


class ExternalWorkflowSubmitAction(OARepoSubmitAction):
    def apply(self, identity, request_type, topic, uow, *args, **kwargs):
        data = {
            "draftId": topic['id'],
            "requestId": str(self.request.id)
        }
        headers = get_ingest_headers()
        hostname = current_app.config['INGEST_API_HOSTNAME']
        # TODO Store cluster workflow template Id in the metadata 'simple-dag'
        response = requests.post(f"{hostname}/api/v1/ingest/batch/simple/basic-ingest", json=data, headers=headers)
        response.raise_for_status()
        return response


class ExternalWorkflowDeclineAction(OARepoDeclineAction):
    def apply(self, identity, request_type, topic, uow, *args, **kwargs):
        print(f"External workflow was declined")

class ExternalWorkflowAcceptAction(OARepoAcceptAction):

    def apply(self, identity, request_type, topic, uow, *args, **kwargs):
        print(f"External workflow finished successfully")
