from oarepo_ui.resources.components import BabelComponent, PermissionsComponent
from oarepo_ui.resources.components import FilesComponent, AllowedHtmlTagsComponent
from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources.resource import RecordsUIResource
from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_ui.resources.components import AllowedCommunitiesComponent


class LterResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/lter/"
    blueprint_name = "lter"
    ui_serializer_class = "lter.resources.records.ui.LterUIJSONSerializer"
    api_service = "lter"
    search_component = "lter/search/ResultsListItem"

    components = [
        # AllowedHtmlTagsComponent,
        BabelComponent,
        # PermissionsComponent,
        # FilesComponent,
        # AllowedCommunitiesComponent
    ]
    try:
        from oarepo_vocabularies.ui.resources.components import (
            DepositVocabularyOptionsComponent,
        )
        components.append(DepositVocabularyOptionsComponent)
    except ImportError:
        pass

    application_id = "lter"

    templates = {
        "detail": "lter.Detail",
        "search": "lter.Search",
        "edit": "lter.Deposit",
        "create": "lter.Deposit",
    }

    @property
    def exports(self):
        return {
            "iso19139": {
                "name": _("XML"),
                "serializer": "shared.resources.serializers.iso19139:ISO19139Serializer",
                "content-type": "text/xml",
                "filename": "{id}.xml",
            },
        }


class LterResource(RecordsUIResource):
    pass


def create_blueprint(app):
    """Register blueprint for this resource."""
    return LterResource(LterResourceConfig()).as_blueprint()
