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
  "descriptions": {
    "type": "array",
    "label": "Descriptions",
    "items": {
      "type": "object",
      "properties": {
        "description": {
          "type": "string",
          "label": "Description",
          "min-length": 200,
          "max-length": 4000,
          "comment-on-length": "number of characters",
          "TODO": "Choose tooltip",
          "tooltip": "The more elaborate description of the resource. Focus on a content description that makes it easy for others to find, and to interpret its relevance.",
          "tooltip2": "Please describe the dataset with an abstract of at least 200 characters. Please consider giving the description more structure by adding additional description fields.",
          "required": true
        },
        "language": {
          "type": "string"
        },
        "type": {
          "type": "enum",
          "label": "Type",
          "tooltip": "The type of description.",
          "required": true,
          "enumValues": [
            "Abstract",
            "AdditionalInfo",
            "Methods",
            "SeriesInformation",
            "TableOfContents",
            "TechnicalInfo",
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
A brief overview of the resource (e.g. abstract, method). The abstract should include basic information that summarizes the resource
### Multiplicity
1-n
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)