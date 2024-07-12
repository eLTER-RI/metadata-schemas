from invenio_db import db
from invenio_drafts_resources.records import (
    DraftMetadataBase,
    ParentRecordMixin,
    ParentRecordStateMixin,
)
from invenio_records.models import RecordMetadataBase


class LterParentMetadata(db.Model, RecordMetadataBase):

    __tablename__ = "lter_parent_record_metadata"


class LterMetadata(db.Model, RecordMetadataBase, ParentRecordMixin):
    """Model for LterRecord metadata."""

    __tablename__ = "lter_metadata"

    # Enables SQLAlchemy-Continuum versioning
    __versioned__ = {}

    __parent_record_model__ = LterParentMetadata


class LterDraftMetadata(db.Model, DraftMetadataBase, ParentRecordMixin):
    """Model for LterDraft metadata."""

    __tablename__ = "lter_draft_metadata"

    __parent_record_model__ = LterParentMetadata


class LterParentState(db.Model, ParentRecordStateMixin):
    table_name = "lter_parent_state_metadata"

    __parent_record_model__ = LterParentMetadata
    __record_model__ = LterMetadata
    __draft_model__ = LterDraftMetadata
