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
    "label": "Contributor(s)",
    "tooltip": "The list of all other contributors. Please mention all persons that were relevant in the creation of the resource.",
    "required": false,
    "items": {
      "type": "object",
      "properties": {
        "email": {
          "type": "string",
          "required": false
        },
        "familyName": {
          "type": "string",
          "label": "Family name",
          "tooltip": "The family names given to this entity."
        },
        "givenName": {
          "type": "string",
          "label": "Given name",
          "tooltip": "The first names given to this entity."
        },
        "affiliation": {
          "type": "object",
          "properties": {
            "affiliation_name": {
              "type": "string",
              "label": "Affiliation name",
              "tooltip": "Name of the (current) organisation of the author.",
              "required": true
            },
            "affiliation_identifier": {
              "type": "string",
              "label": "Affiliation ID",
              "placeholder": "https://ror.org/000h6jb29",
              "tooltip": "Query https://ror.org/ for the ROR of the organisation",
              "required": false
          }
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
          "type": "enum",
          "enumValue": [
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
Entities that contributes to the resource. 
### Required
optional
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
