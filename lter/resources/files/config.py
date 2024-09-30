import importlib_metadata
from flask_resources import ResponseHandler
from invenio_records_resources.resources import FileResourceConfig

from lter.resources.files.ui import (
    LterFileDraftUIJSONSerializer,
    LterFileUIJSONSerializer,
)


class LterFileResourceConfig(FileResourceConfig):
    """LterFile resource config."""

    blueprint_name = "lter_file"
    url_prefix = "/lter/<pid_value>"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.lter.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                LterFileUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }


class LterFileDraftResourceConfig(FileResourceConfig):
    """LterFileDraft resource config."""

    blueprint_name = "lter_file_draft"
    url_prefix = "/lter/<pid_value>/draft"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.lter.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                LterFileDraftUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
