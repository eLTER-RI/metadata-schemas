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
  "geoServerInfo": {
    "type": "object",
    "properties": {
      "mapData": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "bytetype": {
              "type": "boolean"
            },
            "epsgCode": {
              "type": "integer"
            },
            "features": {
              "type": "object",
              "properties": {
                "label": {
                  "type": "string"
                },
                "name": {
                  "type": "string"
                },
                "style": {
                  "type": "object",
                  "properties": {
                    "colour": {
                      "type": "string"
                    }
                  }
                }
              }
            },
            "path": {
              "type": "string"
            },
            "type": {
              "type": "string"
            }
          }
        }
      },
      "serviceType": {
        "type": "string"
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