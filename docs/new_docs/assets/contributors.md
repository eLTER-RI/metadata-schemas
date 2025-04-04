[Back to model](_base.md)

# Name

- **[Schema](#schema)**
- **[Description](#description)**
- **[ISO Mapping](#iso-mapping)**
- **[Provenance](#provenance)**
- **[JSON Example](#json-example)**
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
        "contributorEmail": {
          "type": "string",
          "required": false
        },
        "contributorFamilyName": {
          "type": "string",
          "label": "Family name",
          "tooltip": "The family names given to this entity."
        },
        "contributorGivenName": {
          "type": "string",
          "label": "Given name",
          "tooltip": "The first names given to this entity."
        },
        "contributorAffiliation": {
          "type": "object",
          "properties": {
            "entityName": {
              "type": "string",
              "label": "Affiliation name",
              "tooltip": "Name of the (current) organisation of the author.",
              "required": true
            },
            "entityID": {
              "type": "object",
              "properties": {
                "entityID": {
                  "type": "string"
                },
                "entityIDSchema": {
                  "type": "string"
                }
              }
            }
          }
        },
        "contributorIDs": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "entityID": {
                "type": "string"
              },
              "entityIDSchema": {
                "type": "string"
              }
            }
          }
        },
        "contributorType": {
          "type": "string",
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
[0..n]

### RDF Property
_None_

### EML Element
_None_

## ISO Mapping

## Provenance
_None_

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

## Ingest Form Mapping

[Back to model](_base.md)
