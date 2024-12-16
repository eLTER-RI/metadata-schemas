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
        "email": {
          "type": "string",
          "label": "eMail",
          "tooltip": "Mailaddress of the author"
        },
        "familyName": {
          "type": "string"
        },
        "fullName": {
          "type": "string"
        },
        "givenName": {
          "type": "string"
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
                "values": ["orcid", "ror"],
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
