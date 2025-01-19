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
  "siteReference": {
    "type": "array",
    "label": "eLTER site and platform(s)",
    "tooltip": "Provide the list of site(s) or platform(s) where the dataset has been collected.",
    "requried": true,
    "items": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "PID": {
          "type": "string"
        }
      }
    }
  }
}
```
## Description
### Definition
Reference to the respecitive eLTER facility using the deims.id
### Multiplicity
1-n
### Enumeration
based on the deims.id as provided by the DEIMS-API
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)
