[Back to model](_base.md)

# Name

- **[Schema](#schema)**
- **[Description](#description)**
- **[JSON Example](#json-example)**
- **[ISO Mapping](#iso-mapping)**
---
## Schema
```json
{
  "projects": {
    "type": "array",
    "required": false,
    "items": {
      "type": "object",
      "label": "Project",
      "tooltip": "Information on the project or funding source for the resource."
      "properties": {
        "name": {
          "type": "string"
        },
        "url": {
          "type": "string"
        },
        "project_identifier": {
          "type": "string",
          "label": "Project identifier",
          "tooltip": "Persistent identifier (e.g. CORDIS-ID, DOI) for the project.",
          "required": false
        }
      }
    }
  }
}
```
## Description
### Definition
The project field contains information on the project in which this dataset was collected; e.g. CORDIS-ID
### Required
optional
### Multiplicity
0-n
### RDF Property
prov:Activity
### EML URL
https://eml.ecoinformatics.org/schema/eml-dataset_xsd.html#DatasetType_project
## JSON Example
```json
"projects": [
  {
  "name": "project1",
  "url": "https://www.project1.org"
  },
  {
  "name": "project2",
  "id": "https://www.project2.org"
  }
```

## ISO Mapping

[Back to model](_base.md)
