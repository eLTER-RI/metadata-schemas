from lter.files.api import LterFileDraft
from lter.files.requests.resolvers import LterFileDraftResolver
from lter.records.api import LterDraft, LterRecord
from lter.records.requests.delete_record.types import DeleteRecordRequestType
from lter.records.requests.edit_record.types import EditRecordRequestType
from lter.records.requests.publish_draft.types import PublishDraftRequestType
from lter.records.requests.resolvers import LterDraftResolver, LterResolver
from lter.resources.files.config import (
    LterFileDraftResourceConfig,
    LterFileResourceConfig,
)
from lter.resources.files.resource import LterFileDraftResource, LterFileResource
from lter.resources.records.config import LterResourceConfig
from lter.resources.records.resource import LterResource
from lter.services.files.config import LterFileDraftServiceConfig, LterFileServiceConfig
from lter.services.files.service import LterFileDraftService, LterFileService
from lter.services.records.config import LterServiceConfig
from lter.services.records.service import LterService
from oarepo_requests.resolvers.ui import (
    FallbackEntityReferenceUIResolver,
    GroupEntityReferenceUIResolver,
    RecordEntityDraftReferenceUIResolver,
    RecordEntityReferenceUIResolver,
    UserEntityReferenceUIResolver,
)
from oarepo_requests.resources.draft.resource import DraftRecordRequestsResource
from oarepo_requests.services.draft.service import DraftRecordRequestsService
from oarepo_runtime.records.entity_resolvers import GroupResolver, UserResolver

LTER_RECORD_RESOURCE_CONFIG = LterResourceConfig


LTER_RECORD_RESOURCE_CLASS = LterResource


LTER_RECORD_SERVICE_CONFIG = LterServiceConfig


LTER_RECORD_SERVICE_CLASS = LterService


LTER_REQUESTS_RESOURCE_CLASS = DraftRecordRequestsResource


LTER_REQUESTS_SERVICE_CLASS = DraftRecordRequestsService


REQUESTS_REGISTERED_TYPES = [
    DeleteRecordRequestType(),
    EditRecordRequestType(),
    PublishDraftRequestType(),
]


REQUESTS_ENTITY_RESOLVERS = [
    UserResolver(),
    GroupResolver(),
    LterResolver(record_cls=LterRecord, service_id="lter", type_key="lter"),
    LterDraftResolver(record_cls=LterDraft, service_id="lter", type_key="lter_draft"),
    LterFileDraftResolver(
        record_cls=LterFileDraft,
        service_id="lter_file_draft",
        type_key="lter_file_draft",
    ),
]


ENTITY_REFERENCE_UI_RESOLVERS = {
    "user": UserEntityReferenceUIResolver("user"),
    "fallback": FallbackEntityReferenceUIResolver("fallback"),
    "group": GroupEntityReferenceUIResolver("group"),
    "lter": RecordEntityReferenceUIResolver("lter"),
    "lter_draft": RecordEntityDraftReferenceUIResolver("lter_draft"),
}
REQUESTS_UI_SERIALIZATION_REFERENCED_FIELDS = ["created_by", "receiver", "topic"]


LTER_FILES_RESOURCE_CONFIG = LterFileResourceConfig


LTER_FILES_RESOURCE_CLASS = LterFileResource


LTER_FILES_SERVICE_CONFIG = LterFileServiceConfig


LTER_FILES_SERVICE_CLASS = LterFileService


LTER_DRAFT_FILES_RESOURCE_CONFIG = LterFileDraftResourceConfig


LTER_DRAFT_FILES_RESOURCE_CLASS = LterFileDraftResource


LTER_DRAFT_FILES_SERVICE_CONFIG = LterFileDraftServiceConfig


LTER_DRAFT_FILES_SERVICE_CLASS = LterFileDraftService
