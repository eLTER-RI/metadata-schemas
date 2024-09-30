import marshmallow as ma
from marshmallow import Schema


class LterFileSchema(Schema):
    class Meta:
        unknown = ma.RAISE
