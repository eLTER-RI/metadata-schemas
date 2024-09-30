from invenio_db import db
from invenio_records.models import RecordMetadataBase
from invenio_records_resources.records import FileRecordModelMixin

from lter.records.models import LterDraftMetadata, LterMetadata


class LterFileMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for LterFile metadata."""

    __tablename__ = "lter_file_metadata"
    __record_model_cls__ = LterMetadata


class LterFileDraftMetadata(db.Model, RecordMetadataBase, FileRecordModelMixin):
    """Model for LterFileDraft metadata."""

    __tablename__ = "lter_file_draft_metadata"
    __record_model_cls__ = LterDraftMetadata
