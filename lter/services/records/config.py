from invenio_drafts_resources.services import (
    RecordServiceConfig as InvenioRecordDraftsServiceConfig,
)
from invenio_records_resources.services import (
    ConditionalLink,
    RecordLink,
    pagination_links,
)
from invenio_records_resources.services.records.components import DataComponent
from oarepo_runtime.records import has_draft, is_published_record
from oarepo_runtime.services.components import OwnersComponent
from oarepo_runtime.services.config.service import PermissionsPresetsConfigMixin

from lter.records.api import LterDraft, LterRecord
from lter.services.records.permissions import LterPermissionPolicy
from lter.services.records.results import LterRecordItem, LterRecordList
from lter.services.records.schema import LterSchema
from lter.services.records.search import LterSearchOptions


class LterServiceConfig(
    PermissionsPresetsConfigMixin, InvenioRecordDraftsServiceConfig
):
    """LterRecord service config."""

    result_item_cls = LterRecordItem

    result_list_cls = LterRecordList

    # TODO make it read_only
    # PERMISSIONS_PRESETS = ["read_only"]
    PERMISSIONS_PRESETS = ["everyone"]

    url_prefix = "/lter/"

    base_permission_policy_cls = LterPermissionPolicy

    schema = LterSchema

    search = LterSearchOptions

    record_cls = LterRecord

    service_id = "lter"

    components = [
        *PermissionsPresetsConfigMixin.components,
        *InvenioRecordDraftsServiceConfig.components,
        OwnersComponent,
        DataComponent,
    ]

    model = "lter"
    draft_cls = LterDraft
    search_drafts = LterSearchOptions

    @property
    def links_item(self):
        return {
            "draft": RecordLink("{+api}/lter/{id}/draft"),
            "edit_html": RecordLink("{+ui}/lter/{id}/edit", when=has_draft),
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
