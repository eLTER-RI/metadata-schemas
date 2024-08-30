from oarepo_requests.resolvers.ui import (
    RecordEntityDraftReferenceUIResolver,
    RecordEntityReferenceUIResolver,
)
from oarepo_requests.resources.draft.resource import DraftRecordRequestsResource
from oarepo_requests.services.draft.service import DraftRecordRequestsService

from lter.records.api import LterDraft, LterRecord
from lter.records.requests.resolvers import LterDraftResolver, LterResolver
from lter.resources.records.config import LterResourceConfig
from lter.resources.records.resource import LterResource
from lter.services.records.config import LterServiceConfig
from lter.services.records.service import LterService

LTER_RECORD_RESOURCE_CONFIG = LterResourceConfig


LTER_RECORD_RESOURCE_CLASS = LterResource


LTER_RECORD_SERVICE_CONFIG = LterServiceConfig


LTER_RECORD_SERVICE_CLASS = LterService


OAREPO_PRIMARY_RECORD_SERVICE = {LterRecord: "lter", LterDraft: "lter"}


LTER_REQUESTS_RESOURCE_CLASS = DraftRecordRequestsResource


LTER_REQUESTS_SERVICE_CLASS = DraftRecordRequestsService


LTER_ENTITY_RESOLVERS = [
    LterResolver(record_cls=LterRecord, service_id="lter", type_key="lter"),
    LterDraftResolver(record_cls=LterDraft, service_id="lter", type_key="lter_draft"),
]


ENTITY_REFERENCE_UI_RESOLVERS = {
    "lter": RecordEntityReferenceUIResolver("lter"),
    "lter_draft": RecordEntityDraftReferenceUIResolver("lter_draft"),
}
REQUESTS_UI_SERIALIZATION_REFERENCED_FIELDS = []
