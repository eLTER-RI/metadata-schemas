import marshmallow as ma
from oarepo_runtime.services.schema.ui import InvenioUISchema


class LterFileUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE


class LterFileDraftUISchema(InvenioUISchema):
    class Meta:
        unknown = ma.RAISE
