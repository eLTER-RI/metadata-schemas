[Back to model](_base.md)

# Name

- **[Schema](#schema)**
- **[Description](#description)**
- **[JSON Example](#json-example)**
- **[ISO Mapping](#iso-mapping)**
- **[Ingest form mapping](#ingest-form-mapping)**
---
## Schema
```json
{
  "contributors": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "email": {
          "type": "string"
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
                "type": "string"
              },
              "url": {
                "type": "string"
              }
            }
          }
        },
        "type": {
          "type": "string",
          "valueFrom": [
            "ContactPerson",
            "DataCollector",
            "DataCurator",
            "DataManager",
            "MetadataProvider",
            "Producer",
            "ProjectLeader",
            "ProjectManager",
            "ProjectMember",
            "RegistrationAuthority",
            "RelatedPerson",
            "Researcher",
            "ResearchGroup",
            "Other"
          ]
        }
      }
    }
  }
}
```
## Description
### Definition
Entities that contributes to the dataset. 
### Multiplicity
0 - n
### RDF Property
### EML URL

## JSON Example
```json
{
  "contributors": [
    {
      "fullName": "GivenName MiddleName FamilyName",
      "givenName": "Name1",
      "familyName": "Name2",
      "email": "randomEmail@gmail.com",
      "type": "MetadataProvider",
      "ids": [
        {
          "id": "12345",
          "schema": "Orcid",
          "url": "www.google.com"
        }
      ]
    }
  ]
}
```
## ISO Mapping
## Ingest Form Mapping


[Back to model](_base.md)