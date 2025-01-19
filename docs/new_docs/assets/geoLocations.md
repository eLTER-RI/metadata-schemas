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
        "observationLocation": {
          "type": "object",
          "label": "DEIMS Observation Location ID",
          "properties": {
            "deimsLocationID": {
              "type": "string",
              "placeholder": "i.e. d16ba1ca-b5d7-40b5-8fae-8657543c450b"
            },
            "deimsLocationName": {
              "type": "string"
            }
          }
        },
        "geographicDescription": {
          "type": "string",
          "label": "Place",
          "tooltip": "The name of a place or location."
        },
        "boundingPolygon": {
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
        },
        "boundingBox": {
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
        "point": {
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
### Required
mandatory
### Multiplicity
1-n / still needs to be discussed
### RDF Property
dcterms:spatial
### EML URL
https://eml.ecoinformatics.org/schema/eml-coverage_xsd#Coverage_geographicCoverage
## JSON Example
## ISO Mapping

[Back to model](_base.md)
