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
  "responsibleOrganisations": {
    "type" "array",
    "label": "Responsible Organisations",
    "definition": "Responsible organisation and contact information owning the resource.",
    "tooltip": "Responsible organisation and contact information owning the resource.",
    "required": true,
    "items": {
      "type": "object",
      "properties": {
        "organisationName": {
          "type": "string",
          "label": "Organisation name",
          "tooltip": "Provide the name of the responsible organisation"
        },
        "email": {
          "type": "string",
          "label": "Contact information",
          "tooltip": "Contact email for the resource."
        },
        "organisation_identifier": {
            "type": "string",
            "label": "Organisation ID",
            "placeholder": "https://ror.org/000h6jb29",
            "tooltip": "Provide identifier (e.g. ROR) for the organisation, e.g. https://ror.org/",
            "required": false
          }
        }
      }
    }
  }
```
## Description
### Definition
Responsible organisation and contact information owning the resource.
### Multiplicity
1-n
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)
