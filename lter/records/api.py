from invenio_communities.records.records.systemfields import CommunitiesField
from invenio_drafts_resources.records.api import Draft as InvenioDraft
from invenio_drafts_resources.records.api import DraftRecordIdProviderV2, ParentRecord
from invenio_drafts_resources.records.api import Record as InvenioRecord
from invenio_records.systemfields import ConstantField, ModelField
from invenio_records_resources.records.systemfields import FilesField, IndexField
from invenio_records_resources.records.systemfields.pid import PIDField, PIDFieldContext
from oarepo_communities.records.systemfields.communities import (
    OARepoCommunitiesFieldContext,
)
from oarepo_runtime.records.systemfields.has_draftcheck import HasDraftCheckField
from oarepo_runtime.records.systemfields.owner import OwnersField
from oarepo_runtime.records.systemfields.record_status import RecordStatusSystemField
from oarepo_workflows.records.systemfields.state import RecordStateField
from oarepo_workflows.records.systemfields.workflow import WorkflowField

from lter.files.api import LterFile, LterFileDraft
from lter.records.dumpers.dumper import LterDraftDumper, LterDumper
from lter.records.models import (
    LterCommunitiesMetadata,
    LterDraftMetadata,
    LterMetadata,
    LterParentMetadata,
    LterParentState,
)


class LterParentRecord(ParentRecord):
    model_cls = LterParentMetadata

    workflow = WorkflowField()

    communities = CommunitiesField(
        LterCommunitiesMetadata, context_cls=OARepoCommunitiesFieldContext
    )

    owners = OwnersField()


class LterIdProvider(DraftRecordIdProviderV2):
    pid_type = "lter"


class LterRecord(InvenioRecord):

    model_cls = LterMetadata

    schema = ConstantField("$schema", "local://lter-1.0.0.json")

    index = IndexField(
        "lter-lter-1.0.0",
    )

    pid = PIDField(provider=LterIdProvider, context_cls=PIDFieldContext, create=True)

    dumper = LterDumper()

    state = RecordStateField(initial="published")

    versions_model_cls = LterParentState

    parent_record_cls = LterParentRecord
    record_status = RecordStatusSystemField()
    has_draft = HasDraftCheckField(
        draft_cls=lambda: LterDraft, config_key="HAS_DRAFT_CUSTOM_FIELD"
    )

    files = FilesField(file_cls=LterFile, store=False, create=False, delete=False)

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)


class LterDraft(InvenioDraft):

    model_cls = LterDraftMetadata

    schema = ConstantField("$schema", "local://lter-1.0.0.json")

    index = IndexField("lter-lter_draft-1.0.0", search_alias="lter")

    pid = PIDField(
        provider=LterIdProvider, context_cls=PIDFieldContext, create=True, delete=False
    )

    dumper = LterDraftDumper()

    state = RecordStateField()

    versions_model_cls = LterParentState

    parent_record_cls = LterParentRecord
    record_status = RecordStatusSystemField()

    has_draft = HasDraftCheckField(config_key="HAS_DRAFT_CUSTOM_FIELD")

    files = FilesField(file_cls=LterFileDraft, store=False)

    bucket_id = ModelField(dump=False)
    bucket = ModelField(dump=False)


LterFile.record_cls = LterRecord

LterFileDraft.record_cls = LterDraft
