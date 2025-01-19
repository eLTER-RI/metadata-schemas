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
  "ecosystem": {
    "type": "array",
    "label": "Ecosystem(s)",
    "tooltip": "Provide informaiton on the ecosystem for which the datasource was created.",
    "required": true,
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
Reference to the habitat/ecosystem in which the data source was collected.
### Multiplicity
1-n
### Enumeration
Based on the eLTER CL vocabulary --> https://vocabs.lter-europe.net/elter_cl/en/page/10597
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)
