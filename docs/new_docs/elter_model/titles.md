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
      "title": {
        "type": "string",
        "label": "Title",
        "required": true
      },
      "titleType": {
        "type": "enum",
        "label": "Type",
        "tooltip": "The type of title.",
        "enum": [
          "Title",
          "Alternative Title",
          "Subtitle",
          "Translated Title",
          "Other"
        ],
        "required": true,
        "default": "Title"
      },
      "type": "object",
      "properties": {
        "language": {
          "type": "string",
          "enum": [
            "en",
            "de",
            "..."
          ],
          "comment": "values should be taken from ISO 639-1 and 639-3 language codes",
          "required": "true",
          "tooltip": "Set language for the title",
          "default": "en"
        }
      }
    }
  }
}

```

## Description
### Definition
A name given to the resource. 
### Required
mandatory
### Multiplicity
1
### RDF Property
dcterms:title
### EML URL
https://eml.ecoinformatics.org/schema/eml-resource_xsd.html#ResourceGroup_title

## JSON Example
```json
{
  "titles": [
    {
      "text": "This is a title of the ",
      "titletype": "Title",
      "language": "eng"
    }
  ]
}
```

## ISO Mapping
## Ingest Form Mapping


[Back to model](_base.md)
