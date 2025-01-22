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
  "taxonomicCoverages": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "taxonomicClassification": {
          "type": "object",
          "properties": {
            "taxonomicClassificationID": {
              "type": "string"
            },
            "taxonomicCommonName": {
              "type": "string"
            },
            "taxonomicRankName": {
              "type": "string"
            },
            "taxonomicRankValue": {
              "type": "string"
            }
          }
        },
        "taxonomicDescription": {
          "type": "string"
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