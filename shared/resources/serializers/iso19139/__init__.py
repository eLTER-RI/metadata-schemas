# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 CERN
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""GeoJSON Serializers for Invenio RDM Records."""

from flask_resources import BaseListSchema, MarshmallowSerializer
from flask_resources.serializers import SimpleSerializer

from .schema import ISO19139Schema
from .iso191359serializer import generate_xml


class ISO19139Serializer(MarshmallowSerializer):
    """Marshmallow based GeoJSON serializer for records."""

    def __init__(self, **options):
        """Constructor."""
        super().__init__(
            format_serializer_cls=SimpleSerializer,
            object_schema_cls=ISO19139Schema,
            list_schema_cls=BaseListSchema,
            schema_kwargs={},
            encoder=generate_xml,
        )


