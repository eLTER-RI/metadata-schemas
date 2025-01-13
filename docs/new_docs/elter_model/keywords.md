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
  "keywords": {
    "type": "array",
    "label": "Keywords",
    "tooltip": "The keywords or key phrases describing the resource.",
    "items": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "url": {
          "type": "string"
        }
      }
    }
  }
}
```
## Description
### Definition
A keyword or tag describing the resource.
### Required
mandatory
### Multiplicity
1-n
### RDF Property
dcat:keyword
### EML URL
https://eml.ecoinformatics.org/schema/eml-resource_xsd.html#ResourceGroup_keywordSet
## JSON Example
## ISO Mapping

[Back to model](_base.md)
