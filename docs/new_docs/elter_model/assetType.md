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
  "assetType": {
    "type": "object",
    "required": true,
    "properties": {
      "name": {
        "type": "string",
        "label": "Assent type",
        "tooltip": "Provide the information on the relevant eLTER Standard Observation."
      },
      "url": {
        "type": "string"
      }
    }
  }
}
```
## Description
### Definition
Type of asset based on the list of the eLTER Standard Observations.
### Multiplicity
1
### Required
true
### Enumeration
based on the list of eLTER Standard Observations --> https://vocabs.lter-europe.net/so/en/

For the current implementation the following 6 eLTER Standard Observations are implemented as enumeration (name & url):
"SOGEO_001 Soil inventory – geological characterization" (https://vocabs.lter-europe.net/so/001)
"SOATM_027 Meteorology" (https://vocabs.lter-europe.net/so/027)
"SOBIO_017 Vegetation composition" (https://vocabs.lter-europe.net/so/017)
"SOBIO_096 Surface water – Algae" (https://vocabs.lter-europe.net/so/096)
"SOHYD_004 Physical/chemical characteristics standing waters" (https://vocabs.lter-europe.net/so/004) 
"SOHYD_168 Soil water content and temperature" (https://vocabs.lter-europe.net/so/168)
"Other"
### RDF Property
### EML URL

## JSON Example
## ISO Mapping


[Back to model](_base.md)
