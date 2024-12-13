from invenio_records_resources.services import FileLink, LinksTemplate, RecordLink
from oarepo_runtime.services.components import (
    CustomFieldsComponent,
    process_service_configs,
)
from oarepo_runtime.services.config import (
    has_file_permission,
    has_permission_file_service,
)

from lter.records.api import LterDraft, LterRecord
from lter.services.files.schema import LterFileSchema
from lter.services.records.permissions import LterPermissionPolicy
from shared.services.files.config import ELterServiceConfig


class LterFileServiceConfig(ELterServiceConfig):
    """LterRecord service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/lter/<pid_value>"

    base_permission_policy_cls = LterPermissionPolicy

    schema = LterFileSchema

    record_cls = LterRecord

    service_id = "lter_file"

    search_item_links_template = LinksTemplate
    allowed_mimetypes = []
    allowed_extensions = []
    allow_upload = False

    @property
    def components(self):
        components_list = []
        components_list.extend(process_service_configs(type(self).mro()[2:]))
        additional_components = [CustomFieldsComponent]
        components_list.extend(additional_components)
        seen = set()
        unique_components = []
        for component in components_list:
            if component not in seen:
                unique_components.append(component)
                seen.add(component)

        return unique_components

    model = "lter"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink(
                "{+api}/lter/{id}/files", when=has_permission_file_service("list_files")
            ),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink(
                "{+api}/lter/{id}/files/{key}/commit",
                when=has_permission_file_service("commit_files"),
            ),
            "content": FileLink(
                "{+api}/lter/{id}/files/{key}/content",
                when=has_permission_file_service("get_content_files"),
            ),
            "preview": FileLink("{+ui}/lter/{id}/files/{key}/preview"),
            "self": FileLink(
                "{+api}/lter/{id}/files/{key}",
                when=has_permission_file_service("read_files"),
            ),
        }


class LterFileDraftServiceConfig(ELterServiceConfig):
    """LterDraft service config."""

    PERMISSIONS_PRESETS = ["workflow"]

    url_prefix = "/lter/<pid_value>/draft"

    schema = LterFileSchema

    record_cls = LterDraft

    service_id = "lter_file_draft"

    search_item_links_template = LinksTemplate

    @property
    def components(self):
        components_list = []
        components_list.extend(process_service_configs(type(self).mro()[2:]))
        additional_components = [CustomFieldsComponent]
        components_list.extend(additional_components)
        seen = set()
        unique_components = []
        for component in components_list:
            if component not in seen:
                unique_components.append(component)
                seen.add(component)

        return unique_components

    model = "lter"

    @property
    def file_links_list(self):
        return {
            "self": RecordLink(
                "{+api}/lter/{id}/draft/files", when=has_file_permission("list_files")
            ),
        }

    @property
    def file_links_item(self):
        return {
            "commit": FileLink(
                "{+api}/lter/{id}/draft/files/{key}/commit",
                when=has_file_permission("commit_files"),
            ),
            "content": FileLink(
                "{+api}/lter/{id}/draft/files/{key}/content",
                when=has_file_permission("get_content_files"),
            ),
            "preview": FileLink("{+ui}/lter/{id}/preview/files/{key}/preview"),
            "self": FileLink(
                "{+api}/lter/{id}/draft/files/{key}",
                when=has_file_permission("read_files"),
            ),
        }
