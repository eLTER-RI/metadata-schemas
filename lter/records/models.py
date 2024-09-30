from invenio_communities.records.records.models import CommunityRelationMixin
from invenio_db import db
from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)
from invenio_files_rest.models import Bucket
from invenio_records.models import RecordMetadataBase
from oarepo_workflows.records.models import RecordWorkflowParentModelMixin
from sqlalchemy_utils import UUIDType


class LterParentMetadata(RecordWorkflowParentModelMixin, db.Model, RecordMetadataBase):

    __tablename__ = "lter_parent_record_metadata"


class LterMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for LterRecord metadata."""

    __tablename__ = "lter_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = LterParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class LterDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for LterDraft metadata."""

    __tablename__ = "lter_draft_metadata"

    __parent_record_model__ = LterParentMetadata
    bucket_id = db.Column(UUIDType, db.ForeignKey(Bucket.id))
    bucket = db.relationship(Bucket)


class LterCommunitiesMetadata(db.Model, CommunityRelationMixin):
    __tablename__ = "lter_communities_metadata"
    __record_model__ = LterParentMetadata


class LterParentState(db.Model, ParentRecordStateMixin):
    table_name = "lter_parent_state_metadata"

    __parent_record_model__ = LterParentMetadata
    __record_model__ = LterMetadata
    __draft_model__ = LterDraftMetadata
