from oarepo_ui.resources import BabelComponent
from oarepo_ui.resources.config import RecordsUIResourceConfig
from oarepo_ui.resources.resource import RecordsUIResource


class LterResourceConfig(RecordsUIResourceConfig):
    template_folder = "templates"
    url_prefix = "/lter/"
    blueprint_name = "lter"
    ui_serializer_class = "lter.resources.records.ui.LterUIJSONSerializer"
    api_service = "lter"
    search_component = "lter/search/ResultsListItem.jsx"

    components = [BabelComponent]
    try:
        from oarepo_vocabularies.ui.resources.components import (
            DepositVocabularyOptionsComponent,
        )
        components.append(DepositVocabularyOptionsComponent)
    except ImportError:
        pass

    application_id="lter"

    templates = {
        "detail": "lter.Detail",
        "search": "lter.Search",
        "edit": "lter.Deposit",
        "create":"lter.Deposit",
    }


class LterResource(RecordsUIResource):
    pass


def create_blueprint(app):
    """Register blueprint for this resource."""
    return LterResource(LterResourceConfig()).as_blueprint()
