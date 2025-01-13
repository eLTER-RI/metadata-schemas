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
    "label": "Temporal coverage(s)",
    "tooltip": "The temporal coverage of the contents of the resource.",
    "items": {
      "type": "object",
      "properties": {
        "endDate": {
          "type": "string",
          "label": "End date",
          "tooltip": "The end date and time of the range covered by the resource.",
          "format": "date"
        },
        "startDate": {
          "type": "string",
          "label": "Start date",
          "tooltip": "The start date and time of the range covered by the resource.", 
          "format": "date"
        }
      }
    }
  },
  "temporalResolution": {
    "required": false,
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
