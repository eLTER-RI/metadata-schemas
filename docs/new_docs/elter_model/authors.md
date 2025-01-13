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
    "label": "Creators",
    "tooltip": "The full name of the creators and/or owners of the dataset. The personal name format should be: family, given (e.g.: Smith, John).",
    "items": {
      "type": "object",
      "properties": {
        "givenName": {
          "type": "string",
          "label": "Given name",
          "tooltip": "The first names given to this entity."
        },
        "familyName": {
          "type": "string",
          "label": "Family name",
          "tooltip": "The family names given to this entity.",
          "required": true
        },
        "email": {
          "type": "string",
          "label": "eMail",
          "tooltip": "Contact email address of the author.",
          "required": true
        },
        "affiliation": {
          "type": "object",
          "properties": {
            "affiliation_name": {
              "type": "string",
              "label": "Affiliation",
              "tooltip": "Name of the (current) organisation of the author.",
              "required": true
            },
            "affiliation_identifier": {
              "type": "string",
              "label": "ROR Identifier",
              "placeholder": "https://ror.org/000h6jb29",
              "tooltip": "Query https://ror.org/ for the ROR of the organisation",
              "required": true
          }
        },
        "nameIdentifiers": {
          "type": "array",
          "required": false,
          "items": {
            "type": "object",
            "properties": {
              "name_identifier": {
                "TODO": "id looks better, shorter -> it is under the nameIdentifiers...",
                "type": "string [uri]",
                "label": "Name identifier",
                "tooltip": "The unique identifier of the entity, according to various identifier schemes."
              },
              "schema": {
                "type": "enum",
                "label": "Scheme",
                "tooltip": "The scheme used for the identifier.",
                "default": "orcid",
                "enum": [
                  "orcid",
                  "wob",
                  "scopus"
                ]
              },
              "url": {
                "type": "string",
                "TODO": "This is better to save whole url - no need to parse"
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
The entity (person/people/organisation(s)) responsible for creating the resource.
### Required
mandatory
### Multiplicity
1 - n
### RDF Property
dcterms:creator
### EML URL
https://eml.ecoinformatics.org/schema/eml-resource_xsd.html#ResourceGroup_creator
## JSON Example
```json
{
  "authors/creators": [
    {
      "givenName": "Name1",
      "familyName": "Name2",
      "email": "randomEmail@gmail.com",
      "ids": [
        {
          "TODO": "Check bellow",
          "id": "12345 / https://orcid.org/0000-0003-0631-8231 -- NO!!!",
          "schema": "Orcid",
          "url": "https://orcidXYZ.com -- https://orcid.org/0000-0003-0631-8231 -- YES"
        }
      ]
    }
  ]
}
```
## ISO Mapping
## Ingest Form Mapping


[Back to model](_base.md)
