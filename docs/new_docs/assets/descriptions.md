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
        "descriptionText": {
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
        "descriptionType": {
          "type": "string",
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
### Required
mandatory
### Multiplicity
1-n
### RDF Property
dcterms:description
### EML URL
https://eml.ecoinformatics.org/schema/eml-resource_xsd.html#ResourceGroup_abstract
## JSON Example
```json
{
  "descriptions": {
    "description": "lorem ipsum ...",
    "language": "en",
    "type": "Abstract"
  },
  {
    "description": "the data was collected by ...",
    "language": "en",
    "type": "Method"
  }
}
```
## ISO Mapping

[Back to model](_base.md)
