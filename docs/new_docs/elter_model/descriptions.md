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
  "descriptions": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "description": {
          "type": "string",
          "required": true
        },
        "language": {
          "type": "string"
        },
        "type": {
          "type": "enum",
          "required": true,
          "enumValues": [
            "Abstract",
            "AdditionalInfo",
            "Methods",
            "SeriesInformation",
            "TableOfContents",
            "TechnicalInfo",
            "Other"
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