[Back to model](_base.md)

# Name

- **[Schema](#schema)**
- **[Description](#description)**
- **[ISO Mapping](#iso-mapping)**
- **[Provenance](#provenance)**
- **[JSON Example](#json-example)**
- **[Ingest form mapping](#ingest-form-mapping)**

---

## Schema
```json
{
  "alternateIdentifiers": {
    "type": "array",
    "label": "Alternate identifier(s)",
    "tooltip": "The alternative identifiers for this resource such as a URN, URI or an ISBN number.",
    "items": {
      "type": "object",
      "properties": {
        "alternateID": {
          "type": "string",
          "label": "Alternate identifier",
          "tooltip": "Please provide the reference/identifier to the related resource."
        },
        "alternateIDType": {
          "type": "string",
          "label": "Related Identifier Type",
          "tooltip": "The type of identifier.",
          "enumValues": ["ARK", "arXiv", "bibcode", "DOI", "EAN13", "EISSN", "Handle", "ISBN", "ISSN", "ISTC", "LISSN", "LSID", "ORCID", "PMID", "PURL", "UPC", "URL", "URN", "w3id", "URI"]
        }
      }
    }
  }
}
```

## Description
### Definition
An identifier of other resource related with the one described here.
### Discussion
see also [datasetIds.md](datasetIds.md) which is describing the same MD element. so one of them could be deleted.
### Required
optional

### Multiplicity
[0..n]

### RDF Property
[adms:identifier](https://www.w3.org/TR/vocab-adms/#adms-identifier)

### EML Element
_None_

## ISO Mapping

## Provenance
_None_

## JSON Example

## Ingest Form Mapping

[Back to model](_base.md)
