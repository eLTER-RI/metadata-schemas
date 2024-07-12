import importlib_metadata
from flask_resources import ResponseHandler
from invenio_drafts_resources.resources import RecordResourceConfig

from lter.resources.records.ui import LterUIJSONSerializer


class LterResourceConfig(RecordResourceConfig):
    """LterRecord resource config."""

    blueprint_name = "lter"
    url_prefix = "/lter/"

    @property
    def response_handlers(self):
        entrypoint_response_handlers = {}
        for x in importlib_metadata.entry_points(
            group="invenio.lter.response_handlers"
        ):
            entrypoint_response_handlers.update(x.load())
        return {
            "application/vnd.inveniordm.v1+json": ResponseHandler(
                LterUIJSONSerializer()
            ),
            **super().response_handlers,
            **entrypoint_response_handlers,
        }
