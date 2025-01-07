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
  "temporalCoverages": {
    "required": "once",
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "endDate": {
          "type": "string",
          "format": "date"
        },
        "startDate": {
          "type": "string",
          "format": "date"
        }
      }
    }
  },
  "temporalResolution": {
    "required": "once",
    "label": "Temporal Resolution",
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "resolution": {
          "required": true,
          "label": "Resolution value",
          "type": "numeric"
        },
        "unit": {
          "required": true,
          "label": "Unit",
          "type": "enum",
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
