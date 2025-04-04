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
  "temporalResolution": {
    "required": false,
    "label": "Temporal Resolution",
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "temporalResolutionValue": {
          "required": true,
          "label": "Resolution value",
          "type": "integer"
        },
        "temporalResolutionUnit": {
          "required": true,
          "label": "Unit",
          "type": "string",
          "enum": [
            "Hz", "Minutes", "Hours", "Days", "Weeks", "Months", "Years"
          ]
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
