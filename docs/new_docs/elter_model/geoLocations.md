[Back to model](_base.md)

# Name

- **[Schema](#schema)**
- **[Description](#description)**
- **[JSON Example](#json-example)**
- **[ISO Mapping](#iso-mapping)**
---
## Schema
```json
{
  "geoLocations": {
    "type": "array",
    "label": "Spatial coverage",
    "tooltip": "The spatial coverages of the contents of the resource.",
    "items": {
      "type": "object",
      "properties": {
        "comment": "one of Polygon/Box/Point/DEIMS Observation Location ID",
        "EX_GeographicDescription": {
          "type": "string",
          "label": "Place",
          "tooltip": "The name of a place or location."
        },
        "DEIMS_Observation_ID": {
          "type": "String",
          "label": "DEIMS Observation Location ID",
          "required": false,
          "placeholder": "i.e. d16ba1ca-b5d7-40b5-8fae-8657543c450b"
        },
        "EX_ObservationLocation": {
          "TODO": "This is the field above, the name is stored in the description",
          "type": "object",
          "label": "Observation location",
          "tooltip": "The related observation location for the eLTER site or platform as defined in DEIMS-SDR.",
          "properties": {
            "name": {
              "type": "string"
            },
            "PID": {
              "type": "string"
            }
          }
        },
        "EX_BoundingPolygon": {
          "type": "array",
          "label": "Polygons",
          "tooltip": "One or more drawn polygon areas, defined by a set of points and lines connecting the points in a closed chain.",
          "items": {
            "type": "object",
            "properties": {
              "inPolygonPoint": {
                "type": "object",
                "properties": {
                  "latitude": {
                    "type": "number",
                    "maximum": 90,
                    "minimum": -90,
                    "tooltip": "Please use WGS 84 notation with a dot as decimal separator, i.e. 51.340199."
                  },
                  "longitude": {
                    "type": "number",
                    "maximum": 180,
                    "minimum": -180,
                    "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 12.360103."
                  }
                }
              },
              "points": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "latitude": {
                      "type": "number",
                      "maximum": 90,
                      "minimum": -90,
                      "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 51.340199.",
                    },
                    "longitude": {
                      "type": "number",
                      "maximum": 180,
                      "minimum": -180,
                      "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 12.360103.",
                    }
                  }
                }
              }
            }
          }
        },
        "EX_GeographicBoundingBox": {
          "type": "object",
          "label": "Box",
          "tooltip": "A bounding box defined by two points.",
          "properties": {
            "eastBoundLongitude": {
              "type": "number",
              "maximum": 180,
              "minimum": -180,
              "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 12.360103."
            },
            "northBoundLatitude": {
              "type": "number",
              "maximum": 90,
              "minimum": -90,
              "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 51.340199."
            },
            "southBoundLatitude": {
              "type": "number",
              "maximum": 90,
              "minimum": -90,
              "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 51.340199."
            },
            "westBoundLongitude": {
              "type": "number",
              "maximum": 180,
              "minimum": -180,
              "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 12.360103."
            }
          }
        },
        "Point": {
          "type": "object",
          "label": "Point",
          "tooltip": "A point contains a single latitude-longitude pair.",
          "properties": {
            "latitude": {
              "type": "number",
              "maximum": 90,
              "minimum": -90,
              "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 51.340199."
            },
            "longitude": {
              "type": "number",
              "maximum": 180,
              "minimum": -180,
              "tooltip": "Please use WGS84 notation with a dot as decimal separator, i.e. 12.360103."
            }
          }
        }
      }
    }
  }
}
```

## Description
### Definition
The spatial coverages of the contents of the resource.
### Multiplicity
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)