[Back to model](_base.md)

# Authors

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
  "creators": {
    "type": "array",
    "label": "Creators",
    "tooltip": "The full name of the creators and/or owners of the dataset. The personal name format should be: family, given (e.g.: Smith, John).",
    "items": {
      "type": "object",
      "properties": {
        "creatorGivenName": {
          "type": "string",
          "label": "Given name",
          "tooltip": "The first names given to this entity."
        },
        "creatorFamilyName": {
          "type": "string",
          "label": "Family name",
          "tooltip": "The family names given to this entity.",
          "required": true
        },
        "creatorEmail": {
          "type": "string",
          "label": "eMail",
          "tooltip": "Contact email address of the author.",
          "required": true
        },
        "creatorAffiliation": {
          "type": "object",
          "properties": {
            "entityName": {
              "type": "string",
              "label": "Organization/Group name",
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
          },
          "creatorIDs": {
            "type": "array",
            "required": false,
            "items": {
              "type": "object",
              "properties": {
                "entityID": {
                  "TODO": "id looks better, shorter -> it is under the nameIdentifiers...",
                  "type": "string [uri]",
                  "label": "Identifier",
                  "tooltip": "The unique identifier of the entity, according to various identifier schemes."
                },
                "entityIDSchema": {
                  "type": "enum",
                  "label": "Scheme",
                  "tooltip": "The scheme used for the identifier.",
                  "default": "orcid",
                  "enum": [
                    "orcid",
                    "wob",
                    "scopus"
                  ]
                }
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
[1..n]

### RDF Property
[dcterms:creator](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_creator)

### EML Element
[creator](https://eml.ecoinformatics.org/schema/eml-resource_xsd.html#ResourceGroup_creator)

## ISO Mapping

## Provenance
This element can be used to capture provenance information by establishing relationships between the dataset and its creator using the property [prov:wasAttributedTo](https://www.w3.org/TR/prov-o/#wasAttributedTo).

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

## Ingest Form Mapping

[Back to model](_base.md)
