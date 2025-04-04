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
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "titleLanguage": {
        "type": "string"
      },
      "titleText": {
        "label": "Title",
        "tooltip": "Title for the resource.",
        "required": true,
        "type": "string"
      }
    }
  }
},
```

## Description
### Definition
A title given to the resource. 
### Required
mandatory

### Multiplicity
[1]

### RDF Property
[dcterms:title](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_relation)

### EML Element
[title](https://eml.ecoinformatics.org/schema/eml-resource_xsd.html#ResourceGroup_title)

## ISO Mapping

## Provenance
_None_

## JSON Example
```json
{
  "title": "This is the title of the resource."
}
```

## Ingest Form Mapping


[Back to model](_base.md)
