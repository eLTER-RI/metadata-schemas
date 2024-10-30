from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_drafts_resources.services.records.components import DraftFilesComponent
from invenio_records_resources.services import (
    ConditionalLink,
    RecordLink,
    pagination_links,
)
from oarepo_communities.services.components.default_workflow import (
    CommunityDefaultWorkflowComponent,
)
from oarepo_communities.services.components.include import CommunityInclusionComponent
from oarepo_communities.services.links import CommunitiesLinks
from oarepo_runtime.records import has_draft, is_published_record
from oarepo_runtime.services.components import CustomFieldsComponent, OwnersComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin
from oarepo_runtime.services.files import FilesComponent
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

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordDraftsServiceConfig.components,
        LterComponent,
        CommunityDefaultWorkflowComponent,
        CommunityInclusionComponent,
        OwnersComponent,
        DraftFilesComponent,
        FilesComponent,
        CustomFieldsComponent,
        WorkflowComponent,
    ]

    model = "lter"
    draft_cls = LterDraft
    search_drafts = LterSearchOptions

    @property
    def links_item(self):
        return {
            "applicable-requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/lter/{id}/requests/applicable"),
                else_=RecordLink("{+api}/lter/{id}/draft/requests/applicable"),
            ),
            "communities": CommunitiesLinks(
                {
                    "self": "{+api}/communities/{id}",
                    "self_html": "{+ui}/communities/{slug}/records",
                }
            ),
            "draft": RecordLink("{+api}/lter/{id}/draft"),
            "edit_html": RecordLink("{+ui}/lter/{id}/edit", when=has_draft),
            "files": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/lter/{id}/files"),
                else_=RecordLink("{+api}/lter/{id}/draft/files"),
            ),
            "latest": RecordLink("{+api}/lter/{id}/versions/latest"),
            "latest_html": RecordLink("{+ui}/lter/{id}/latest"),
            "publish": RecordLink("{+api}/lter/{id}/draft/actions/publish"),
            "record": RecordLink("{+api}/lter/{id}"),
            "requests": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/lter/{id}/requests"),
                else_=RecordLink("{+api}/lter/{id}/draft/requests"),
            ),
            "self": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+api}/lter/{id}"),
                else_=RecordLink("{+api}/lter/{id}/draft"),
            ),
            "self_html": ConditionalLink(
                cond=is_published_record,
                if_=RecordLink("{+ui}/lter/{id}"),
                else_=RecordLink("{+ui}/lter/{id}/preview"),
            ),
            "versions": RecordLink("{+api}/lter/{id}/versions"),
        }

    @property
    def links_search(self):
        return {
            **pagination_links("{+api}/lter/{?args*}"),
        }

    @property
    def links_search_drafts(self):
        return {
            **pagination_links("{+api}/user/lter/{?args*}"),
        }

    @property
    def links_search_versions(self):
        return {
            **pagination_links("{+api}/lter/{id}/versions{?args*}"),
        }
