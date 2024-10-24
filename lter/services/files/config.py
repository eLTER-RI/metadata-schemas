from invenio_records_resources.services import FileLink, RecordLink
from oarepo_runtime.services.components import CustomFieldsComponent

from lter.records.api import LterDraft, LterRecord
from lter.services.files.schema import LterFileSchema
from lter.services.records.permissions import LterPermissionPolicy
from shared.services.files.config import ELterServiceConfig


class LterFileServiceConfig(ELterServiceConfig):
    """LterRecord service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/lter/<pid_value>"

    base_permission_policy_cls = LterPermissionPolicy

    schema = LterFileSchema

    record_cls = LterRecord

    service_id = "lter_file"

    components = [*ELterServiceConfig.components, CustomFieldsComponent]

    model = "lter"
    allowed_mimetypes = []
    allowed_extensions = []
    allow_upload = False

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/lter/{id}/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/lter/{id}/files/{key}/commit"),
            "content": FileLink("{+api}/lter/{id}/files/{key}/content"),
            "preview": FileLink("{+ui}/lter/{id}/files/{key}/preview"),
            "self": FileLink("{+api}/lter/{id}/files/{key}"),
        }


class LterFileDraftServiceConfig(ELterServiceConfig):
    """LterDraft service config."""

    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/lter/<pid_value>/draft"

    schema = LterFileSchema

    record_cls = LterDraft

    service_id = "lter_file_draft"

    components = [*ELterServiceConfig.components, CustomFieldsComponent]

    model = "lter"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink("{+api}/lter/{id}/draft/files"),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink("{+api}/lter/{id}/draft/files/{key}/commit"),
            "content": FileLink("{+api}/lter/{id}/draft/files/{key}/content"),
            "preview": FileLink("{+ui}/lter/{id}/files/{key}/preview"),
            "self": FileLink("{+api}/lter/{id}/draft/files/{key}"),
        }
