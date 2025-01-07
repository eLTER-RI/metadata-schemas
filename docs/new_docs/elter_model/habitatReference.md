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
    "HabitatReference": {
      "type": "object",
      "label": "Habitat",
      "properties": {
        "so_habitat": {
          "required": true,
          "label": "eLTER Standard Observeation (SO) Habitat",
          "type": "enum",
          "enum": [
            "Wetlands (mires, bogs, fens)",
            "Grasslands and lands dominated by forbs, mosses or lichens",
            "Heathlands, shrub and tundra",
            "Forests and other wooded land",
            "Vegetated man-made habitats (agricultural, horticultural, domestic)",
            "Inland surface standing waters",
            "Coastal (transitional) waters including coastal littoral zones",
            "Sparsely vegetated habitats and deserts"
          ]
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
