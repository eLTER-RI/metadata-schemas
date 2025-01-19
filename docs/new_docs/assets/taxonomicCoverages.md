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
            "commonName": {
              "type": "string"
            },
            "taxonomicClassificationID": {
              "type": "string"
            },
            "rankName": {
              "type": "string"
            },
            "rankValue": {
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