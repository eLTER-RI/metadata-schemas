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
  "methods": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "instrumentationDescription": {
          "type": "string"
        },
        "methodID": {
          "type": "string"
        },
        "qualityControlDescription": {
          "type": "string"
        },
        "sampling": {
          "type": "object",
          "properties": {
            "samplingDescription": {
              "type": "string"
            },
            "studyDescription": {
              "type": "string"
            }
          }
        },
        "steps": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "stepDescription": {
                "type": "string"
              },
              "stepTitle": {
                "type": "string"
              }
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