from oarepo_ui.resources.config import TemplatePageUIResourceConfig
from oarepo_ui.resources.resource import TemplatePageUIResource


class QcPagesResourceConfig(TemplatePageUIResourceConfig):
    url_prefix = "/qc"
    blueprint_name = "ui_quality_checks"
    template_folder = "templates"
    pages = {
        "<pid_value>/report": "QCReportPage",
    }


def create_blueprint(app):
    """Register blueprint for this resource."""
    return TemplatePageUIResource(QcPagesResourceConfig()).as_blueprint()
