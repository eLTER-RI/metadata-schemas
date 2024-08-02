# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Graz University of Technology.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""GeoJSON based Schema for Invenio RDM Records."""

from marshmallow import Schema, fields, INCLUDE


class ISO19139Schema(Schema):
    """Schema for ISO19139 in XML."""

    class Meta:
        unknown = INCLUDE

    metadata = fields.Raw()
    id = fields.Str()
