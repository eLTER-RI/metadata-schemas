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
        "ids": {
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
                "label": Scheme URI",
                "tooltip": "The URI pointing to the scheme.",
                "default": ""url": "https://orcidXYZ.com"
                "
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
  "authors": [
    {
      "fullName": "GivenName MiddleName FamilyName",
      "givenName": "Name1",
      "familyName": "Name2",
      "nameType": "Personal",
      "ids": [
        {
          "id": "[12345](https://orcid.org/0000-0003-0631-8231)",
          "schema": "Orcid",
          "url": "https://orcidXYZ.com"
        }
      ]
    }
  ]
}
```
## ISO Mapping
## Ingest Form Mapping


[Back to model](_base.md)
