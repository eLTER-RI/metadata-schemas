[Back to model](_base.md)

# Titles

- **[Schema](#schema)**
- **[Description](#description)**
- **[JSON Example](#json-example)**
- **[ISO Mapping](#iso-mapping)**
- **[Ingest form mapping](#ingest-form-mapping)**
---
## Schema
```json
{
  "titles": {
    "type": "array",
    "items": {
      "type": "object",
      "properties": {
        "language": {
          "type": "string"
        },
        "text": {
          "type": "string",
          "required": true
        }
      }
    }
  }
}
```

## Description
### Definition
Titles possible in multiple languages of the dataset. 
### Multiplicity
1 - n
### RDF Property
dcterms:title
### EML URL
https://eml.ecoinformatics.org/schema/eml-resource_xsd.html#ResourceGroup_title

## JSON Example
```json
{
  "titles": [
    {
      "language": "eng",
      "text": "This is a title of the "
    }
  ]
}
```

## ISO Mapping
## Ingest Form Mapping


[Back to model](_base.md)