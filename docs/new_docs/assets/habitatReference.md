[Back to model](_base.md)

# Habitat Reference

- **[Schema](#schema)**
- **[Description](#description)**
- **[JSON Example](#json-example)**
- **[ISO Mapping](#iso-mapping)**
---
## Schema
```json
{
  "habitatReference": {
    "type": "array",
    "label": "Related habitats",
    "tooltip": "Provide informaiton on the habitats for which the datasource was created.",
    "required": true,
    "items": {
      "type": "object",
      "properties": {
        "soHabitatCode": {
          "type": "string"
        },
        "soHabitatURI": {
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
```json
"enum": [
    "Wetlands (mires, bogs, fens)",
    "Grasslands and lands dominated by forbs, mosses or lichens",
    "Heathlands, shrub and tundra",
    "Forests and other wooded land",
    "Vegetated man-made habitats (agricultural, horticultural, domestic)",
    "Inland surface standing waters",
    "Inland standing waters",
    "Coastal (transitional) waters including coastal littoral zones",
    "Sparsely vegetated habitats and deserts"
]
```
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)
