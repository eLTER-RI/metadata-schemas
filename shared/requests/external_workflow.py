from oarepo_runtime.i18n import lazy_gettext as _

from oarepo_requests.types.generic import (NonDuplicableOARepoRequestType, OARepoRequestType)
from oarepo_requests.types.ref_types import ModelRefTypes
from .actions import ExternalWorkflowAcceptAction, ExternalWorkflowSubmitAction, ExternalWorkflowDeclineAction


# class ExternalWorkflowRequestType(NonDuplicableOARepoRequestType):
class ExternalWorkflowRequestType(OARepoRequestType):

    type_id = "run_external_workflow"
    name = _("Run external workflow")

    payload_schema = {
    }

    @classmethod
    @property
    def available_actions(cls):
        return {
            **super().available_actions,
            "decline": ExternalWorkflowDeclineAction,
            "submit": ExternalWorkflowSubmitAction,
            "accept": ExternalWorkflowAcceptAction,
        }

    description = _("Request running external workflow on a record")
    receiver_can_be_none = True
    allowed_topic_ref_types = ModelRefTypes(published=True, draft=True)
