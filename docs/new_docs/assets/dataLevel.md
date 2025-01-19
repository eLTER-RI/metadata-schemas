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
  "dataLevel": {
    "label": "Data Level",
    "required": true,
    "TODO": "this will be done with vocabs in the future",
    "tooltip": "Data level according to the eLTER defined data levels.",
    "tooltip2": "TBD - see https://elter.atlassian.net/wiki/spaces/EC/pages/918749186/eLTER+Data+Levels"
    "type": "object" {
      "properties": {
        "name": {
          "type": "enum",
          "enumValues": [
            "0",
            "1",
            "2",
            "3"
          ]
        },
        "url": {
          "type": "string",
          "tooltip": "Provide url to the concept in the eLTER vocabularies.",
          "TODO": "this will be taken automatically from the vocabulary in future"
        }
      }
    }
  }
}
```
## Description
### Definition
Definition of the data levels according to the eLTER definition.
### Multiplicity
1
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)
