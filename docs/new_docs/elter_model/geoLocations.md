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
    "items": {
      "type": "object",
      "properties": {
        "comment": "one of Polygon/Box/Point",
        "EX_BoundingPolygon": {
          "type": "array",
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
        "EX_GeographicDescription": {
          "type": "string"
        },
        "Point": {
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
}
```
## Description
### Definition
### Multiplicity
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)