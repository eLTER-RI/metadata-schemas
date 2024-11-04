import marshmallow as ma
from invenio_records_resources.services.files.schema import (
    FileSchema as InvenioFileSchema,
)
from marshmallow import fields as ma_fields
from oarepo_runtime.services.schema.validation import validate_date


class LterFileSchema(InvenioFileSchema):
    class Meta:
        unknown = ma.RAISE

    created = ma_fields.String(dump_only=True, validate=[validate_date("%Y-%m-%d")])

    updated = ma_fields.String(dump_only=True, validate=[validate_date("%Y-%m-%d")])
