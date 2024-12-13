from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_records_resources.services import (
    ConditionalLink,
    LinksTemplate,
    RecordLink,
    pagination_links,
)
from oarepo_communities.services.components.default_workflow import (
    CommunityDefaultWorkflowComponent,
)
from oarepo_communities.services.components.include import CommunityInclusionComponent
from oarepo_communities.services.links import CommunitiesLinks
from oarepo_runtime.services.components import (
    CustomFieldsComponent,
    OwnersComponent,
    process_service_configs,
)
from oarepo_runtime.services.config import (
    has_draft,
    has_file_permission,
    has_permission,
    has_published_record,
    is_published_record,
)
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent
from oarepo_runtime.services.records import pagination_links_html
from oarepo_workflows.services.components.workflow import WorkflowComponent

from lter.records.api import LterDraft, LterRecord
from lter.services.records.permissions import LterPermissionPolicy
from lter.services.records.results import LterRecordItem, LterRecordList
from lter.services.records.schema import LterSchema
from lter.services.records.search import LterSearchOptions
from shared.services.components.lter_component import LterComponent


class LterServiceConfig(
    PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig
):
    """LterRecord service config."""

    result_item_cls = LterRecordItem

    result_list_cls = LterRecordList

    PERMISSIONS_PRESETS = ["community-workflow"]

    url_prefix = "/lter/"

    base_permission_policy_cls = LterPermissionPolicy

    schema = LterSchema

    search = LterSearchOptions

    record_cls = LterRecord

    service_id = "lter"

    search_item_links_template = LinksTemplate
    draft_cls = LterDraft
    search_drafts = LterSearchOptions

    @property
    def components(self):
        components_list = []
        components_list.extend(process_service_configs(type(self).mro()[2:]))
        additional_components = [
            LterComponent,
            CommunityDefaultWorkflowComponent,
            CommunityInclusionComponent,
            OwnersComponent,
            FilesComponent,
            DraftFilesComponent,
            CustomFieldsComponent,
            WorkflowComponent,
        ]
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
    def links_item(self):
        return {
            "applicable-requests": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/lter/{id}/requests/applicable"),
                else_=RecordLink("{+api}/lter/{id}/draft/requests/applicable"),
            ),
            "communities": CommunitiesLinks(
                {
                    "self": "{+api}/communities/{id}",
                    "self_html": "{+ui}/communities/{slug}/records",
                }
            ),
            "draft": RecordLink(
                "{+api}/lter/{id}/draft",
                when=has_draft() & has_permission("read_draft"),
            ),
            "edit_html": RecordLink(
                "{+ui}/lter/{id}/edit", when=has_draft() & has_permission("update")
            ),
            "files": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink(
                    "{+api}/lter/{id}/files", when=has_file_permission("list_files")
                ),
                else_=RecordLink(
                    "{+api}/lter/{id}/draft/files",
                    when=has_file_permission("list_files"),
                ),
            ),
            "latest": RecordLink(
                "{+api}/lter/{id}/versions/latest", when=has_permission("read")
            ),
            "latest_html": RecordLink(
                "{+ui}/lter/{id}/latest", when=has_permission("read")
            ),
            "publish": RecordLink(
                "{+api}/lter/{id}/draft/actions/publish", when=has_permission("publish")
            ),
            "record": RecordLink(
                "{+api}/lter/{id}", when=has_published_record() & has_permission("read")
            ),
            "requests": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/lter/{id}/requests"),
                else_=RecordLink("{+api}/lter/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/lter/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+api}/lter/{id}/draft", when=has_permission("read_draft")
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+ui}/lter/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+ui}/lter/{id}/preview", when=has_permission("read_draft")
                ),
            ),
            "versions": RecordLink(
                "{+api}/lter/{id}/versions", when=has_permission("search_versions")
            ),
        }

    @property
    def links_search_item(self):
        return {
            "self": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+api}/lter/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+api}/lter/{id}/draft", when=has_permission("read_draft")
                ),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record(),
                if_=RecordLink("{+ui}/lter/{id}", when=has_permission("read")),
                else_=RecordLink(
                    "{+ui}/lter/{id}/preview", when=has_permission("read_draft")
                ),
            ),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/lter/{?args*}"),
            **pagination_links_html("{+ui}/lter/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/lter/{?args*}"),
            **pagination_links_html("{+ui}/user/lter/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/lter/{id}/versions{?args*}"),
        }
