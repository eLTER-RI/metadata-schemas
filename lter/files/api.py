from invenio_records_resources.records.api import FileRecord
from invenio_records_resources.records.systemfields import IndexField

from lter.files.models import LterFileDraftMetadata, LterFileMetadata


class LterFile(FileRecord):

    model_cls = LterFileMetadata

    index = IndexField(
        "lter_file-lter_file-1.0.0",
    )
    record_cls = None  # is defined inside the parent record


class LterFileDraft(FileRecord):

    model_cls = LterFileDraftMetadata

    index = IndexField(
        "lter_file_draft-lter_file_draft-1.0.0",
    )
    record_cls = None  # is defined inside the parent record
