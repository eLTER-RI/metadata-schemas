[Back to model](_base.md)

# Instrumentation

- **[Schema](#schema)**
- **[Description](#description)**
- **[JSON Example](#json-example)**
- **[ISO Mapping](#iso-mapping)**
---
## Schema
```json
{
  "instrumentation": {
    "type": "object",
    "required": "optional",
    "label": "Instrumentation",
    "properties": {
      "description": {
        "type": "string",
        "required": false,
        "min-length": 0,
        "max-length": 4000,
        "comment-on-length": "number of characters",
        "tooltip": "Please describe the instrumentation."
      }
    }
  }
}
```

## Description
### Definition
The scientific instruments the data was generated or captured on.
### Multiplicity
1-n
### RDF Property
sosa:Sensor and prov:Entity
### EML URL
https://eml.ecoinformatics.org/schema/eml-methods_xsd#ProcedureStepType_instrumentation
## JSON Example
## ISO Mapping

[Back to model](_base.md)
