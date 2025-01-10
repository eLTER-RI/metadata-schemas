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
        "comment": "one of Polygon/Box/Point",
        "EX_GeographicDescription": {
          "type": "string",
          "label": "Place",
          "tooltip": "The name of a place or location."
        },
        "EX_ObservationLocation": {
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
                    "minimum": -90
                  },
                  "longitude": {
                    "type": "number"
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
                      "minimum": -90
                    },
                    "longitude": {
                      "type": "number",
                      "maximum": 180,
                      "minimum": -180
                    }
                  }
                }
              }
            }
          }
        },
        "EX_GeographicBoundingBox": {
          "type": "object",
          "label": "Boxes",
          "tooltip": "A bounding box defined by two points.",
          "properties": {
            "eastBoundLongitude": {
              "type": "number",
              "maximum": 180,
              "minimum": -180
            },
            "northBoundLatitude": {
              "type": "number",
              "maximum": 90,
              "minimum": -90
            },
            "southBoundLatitude": {
              "type": "number",
              "maximum": 90,
              "minimum": -90
            },
            "westBoundLongitude": {
              "type": "number",
              "maximum": 180,
              "minimum": -180
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
              "minimum": -90
            },
            "longitude": {
              "type": "number",
              "maximum": 180,
              "minimum": -180
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
