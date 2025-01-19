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
  "externalWorkflow": {
    "type": "object",
    "properties": {
      "defaultWorkflowTemplateId": {
        "type": "string"
      },
      "history": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "date": {
              "type": "string",
              "format": "date-time"
            },
            "status": {
              "type": "string"
            },
            "workflowHandle": {
              "type": "string"
            },
            "workflowTemplateId": {
              "type": "string"
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
### Multiplicity
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)