[Back to model](_base.md)

# Authors

- **[Schema](#schema)**
- **[Description](#description)**
- **[JSON Example](#json-example)**
- **[ISO Mapping](#iso-mapping)**
- **[Ingest form mapping](#ingest-form-mapping)**
---
## Schema
```json
{
  "creators": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "familyName": {
          "type": "string",
          "label": "Family name",
          "tooltip": "The family name given to this entity.",
          "required": false
        },
        "givenName": {
          "type": "string",
          "label": "Given name",
          "tooltip": "The first name given to the entity.",
          "required": false
        },
        "fullName": {
          "type": "string",
          "label": "Full name",
          "tooltip": "The full name of the entity or in case of an organisation the name of the organisation.",
          "required": true
        },
        "nameType": {
          "type": "enum",
          "label": "Name type",
          "tooltip": "The type of the name described.",
          "enum": ["Personal", "Organizational"],
          "required": true,
          "default": "Personal"
        },
        "nameIdentifiers": {
          "type": "array",
          "required": false,
          "items": {
            "type": "object",
            "properties": {
              "name_identifier": {
                "type": "string [uri]",
                "label": "Name identifier",
                "tooltip": "The unique identifier of the entity, according to various identifier schemes."                
              },
              "scheme": {
                "type": "enum",
                "label": "Scheme",
                "tooltip": "The scheme used for the identifier.",
                "default": "orcid",
                "enum": ["orcid", "ror"],
              },
              "schemeUri": {
                "type": "string [uri]",
                "label": "Scheme URI",
                "tooltip": "The URI pointing to the scheme.",
                "default": "https://orcidXYZ.com"
              }
            }
          }
        }
      }
    }
  }
}
```
## Description
### Definition
The entity (person/people/organisation(s)) responsible for creating the dataset
### Multiplicity
1 - n
### RDF Property
dcterms:creator
### EML URL
https://eml.ecoinformatics.org/schema/eml-resource_xsd.html#ResourceGroup_creator
## JSON Example
```json
{
  "creators": [
    {
      "fullName": "Johannes Peterseil",
      "givenName": "Johannes",
      "familyName": "Peterseil",
      "nameType": "Personal",
      "nameIdentifiers": [
        {
          "id": "https://orcid.org/0000-0003-0631-8231",
          "schema": "Orcid",
          "url": "https://orcidXYZ.com"
        }
      ]
    }
  ]
}
{
  "creators": [
    {
      "fullName": "Umweltbundesamt GmbH",
      "nameType": "Organizational",
      "nameIdentifiers": [
        {
          "id": "https://ror.org/013vyke20",
          "schema": "ROR",
          "url": "https://ror.com"
        }
      ]
    }
  ]
}
```
## ISO Mapping
## Ingest Form Mapping


[Back to model](_base.md)
