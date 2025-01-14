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
  "alternateIdentifiers": {
    "type" "array",
    "label": "Alternate identifier(s)",
    "tooltip": "The alternative identifiers for this resource such as a URN, URI or an ISBN number.",
    "items": {
      "type" "object",
      "properties": {
        "sourceName": {
          "type": "string",
          "label": "Name of the original source (e.g. B2SHARE, zenodo) for the resource documented."
        },
        "alternateIdentifier": {
          "type": "string",
          "label": "Alternate identifier",
          "tooltip": "Please provide the reference/identifier to the related resource."
        },
        "alternateIdentifierType": {
          "type": "enum",
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
[0-n]
### RDF Property
### EML URL

## JSON Example
## ISO Mapping

[Back to model](_base.md)
