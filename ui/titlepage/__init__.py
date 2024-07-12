from oarepo_ui.resources import UIResourceConfig
from oarepo_ui.resources.resource import TemplatePageUIResource
from oarepo_ui.resources.components import UIResourceComponent


class CustomComponent(UIResourceComponent):
    def before_render(self, *, extra_context, identity, **kwargs):
        extra_context["KEY"] = "randomValue"


class TitlePageResourceConfig(UIResourceConfig):
    url_prefix = "/"
    blueprint_name = "titlepage"
    template_folder = "templates"
    pages = {
        "": "TitlePage",
    }

    components = [
        CustomComponent
    ]


def create_blueprint(app):
    """Register blueprint for this resource."""
    return TemplatePageUIResource(TitlePageResourceConfig()).as_blueprint()
