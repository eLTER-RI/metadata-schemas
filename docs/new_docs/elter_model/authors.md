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
          "tooltip": "The family names given to this entity."
        },
        "fullName": {
          "type": "string",
          "label": "Full name",
          "tooltip": "The full name of the person or the name of the organisation."
        },
        "email": {
          "type": "string",
          "label": "eMail",
          "tooltip": "Contact email address of the author."
        },
        "nameType": {
          "type": "enum",
          "delfaultValue": "Personal",
          "enumValues":[
            "Personal",
            "Organizational"
          ]
        },
        "ids": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string"
              },
              "schema": {
                "type": "enum",
                "enumValues": [
                  "orcid",
                  "ror"
                ],
              },
              "url": {
                "type": "string"
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
      "email": "randomEmail@gmail.com",
      "ids": [
        {
          "id": "12345",
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
