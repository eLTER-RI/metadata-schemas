[Back to model](_base.md)

**DEPRECATED - needs to be deleted**

# Dataset Ids

- **[Schema](#schema)**
- **[Description](#description)**
- **[JSON Example](#json-example)**
- **[ISO Mapping](#iso-mapping)**
- **[Ingest form mapping](#ingest-form-mapping)**
---
## Schema
```json
{
  "datasetIds": {
    "visibleInForm": False,
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "identifier": {
          "type": "string"
        },
        "sourceName": {
          "type": "string",
          "required": true
        },
        "type": {
          "type": "string"
        },
        "url": {
          "type": "string"
        }
      }
    }
  }
}
```
## Description

## Description
### Definition
Alternative identifiers of the dataset.
### Multiplicity
0 - n
### RDF Property
adms:identifier
### EML URL
_None_
## JSON Example
```json
{
  "datasetIds": [
      {
        "sourceName": "b2share",
        "identifier": "<ANY_ID>",
        "url": "https://b2share.com/<id>",
        "type": "PID"
      }
    ]
}
```
## ISO Mapping
## Ingest Form Mapping


[Back to model](_base.md)
