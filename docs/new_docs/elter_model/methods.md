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
    "type": "object",
    "properties": {
      "PID": {
        "type": "string"
      },
      "instrumentationDescription": {
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
            "description": {
              "type": "string"
            },
            "title": {
              "type": "string"
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