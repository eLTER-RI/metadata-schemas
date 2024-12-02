from oarepo_ui.resources.config import TemplatePageUIResourceConfig
from oarepo_ui.resources.resource import TemplatePageUIResource


class LterDashboardPageResourceConfig(TemplatePageUIResourceConfig):
    url_prefix = "/dashboard"
    blueprint_name = "lter_dashboard"
    template_folder = "templates"
    pages = {
        "": "LterDashboardPage",
    }


def create_blueprint(app):
    """Register blueprint for this resource."""
    return TemplatePageUIResource(LterDashboardPageResourceConfig()).as_blueprint()
