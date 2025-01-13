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
  "temporalCoverages": {
    "required": "once",
    "type": "array",
    "label": "Temporal coverage(s)",
    "tooltip": "The temporal coverage of the contents of the resource.",
    "items": {
      "type": "object",
      "properties": {
        "endDate": {
          "type": "string",
          "label": "End date",
          "tooltip": "The end date and time of the range covered by the resource.",
          "format": "date"
        },
        "startDate": {
          "type": "string",
          "label": "Start date",
          "tooltip": "The start date and time of the range covered by the resource.", 
          "format": "date"
        }
      }
    }
  }
}
```
## Description
### Definition
An interval of time that is named or defined by its start and end.
### Required
mandatory
### Multiplicity
1-n
### RDF Property
dcterms:PeriodOfTime
### EML URL
https://eml.ecoinformatics.org/schema/eml-coverage_xsd#Coverage_temporalCoverage
## JSON Example
## ISO Mapping

[Back to model](_base.md)
