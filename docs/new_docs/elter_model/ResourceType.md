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
  "resource_type": {
    "type": "object",
    "label": "Resource type(s)",
    "tooltip": "The type of ressource(s)",
    "required": true,
    "properties": {
        "resource_type_general": {
        "type": "enum",
        "label": "Resource type",
        "tooltip": "The type of the resource documented.",
        "defaultValue": "Dataset",
        "enumValues": [
          "Audiovisual",
          "Book",
          "BookChapter",
          "Collection",
          "ComputationalNotebook",
          "ConferencePaper",
          "ConferenceProceeding",
          "DataPaper",
          "Dataset",
          "Dissertation",
          "Event",
          "Image",
          "InteractiveResource",
          "Journal",
          "JournalArticle",
          "Model",
          "OutputManagementPlan",
          "PeerReview",
          "PhysicalObject",
          "Preprint",
          "Report",
          "Service",
          "Software",
          "Sound",
          "Standard",
          "Text",
          "Workflow",
          "Other"
        ]
        },
        "reseource_type_description": {
          "type": "string",
          "required": false
        }
     }
  }
}

## Description
### Definition
### Multiplicity
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)
