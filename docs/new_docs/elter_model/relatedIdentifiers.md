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
  "relatedIdentifiers": {
    "type" "array",
    "label": "Related identifiers",
    "tooltip": "The identifiers of other resources related to the resource such as a URN, URI or an ISBN number.",
    "items": {
      "type" "object",
      "properties": {
        "relatedIdentifier": {
          "type": "string",
          "label": "Related identifier",
          "tooltip": "Please provide the reference/identifier to the related resource."
        },
        "resourceType": {
          "type": "enum",
          "enumValues": ["Audiovisual", "Book", "BookChapter", "Collection", "ComputationalNotebook", "ConferencePaper", "ConferenceProceeding", "DataPaper", "Dataset", "Dissertation", "Event", "Image", "InteractiveResource", "Journal", "JournalArticle", "Model", "OutputManagementPlan", "PeerReview", "PhysicalObject", "Preprint", "Report", "Service", "Software", "Sound", "Standard", "Text", "Workflow", "Other"]
        },
        "relatedIdentifierType": {
          "type": "enum",
          "label": "Related Identifier Type",
          "tooltip": "The type of identifier.",
          "enumValues": ["ARK", "arXiv", "bibcode", "DOI", "EAN13", "EISSN", "Handle", "ISBN", "ISSN", "ISTC", "LISSN", "LSID", "ORCID", "PMID", "PURL", "UPC", "URL", "URN", "w3id", "URI"]
        },
        "relationType": {
          "type": "enum",
          "label": "Relation",
          "tooltip": "The relation type of the described reference.",
          "enumValues": ["IsCitedBy", "Cites", "IsSupplementTo", "IsPublishedIn", "IsSupplementedBy", "IsContinuedBy", "Continues", "HasMetadata", "IsMetadataFor", "IsNewVersionOf", "IsPreviousVersionOf", "IsPartOf", "HasPart", "IsReferencedBy", "References", "IsDocumentedBy", "Documents", "isCompiledBy", "Compiles", "IsVariantFormOf", "IsOriginalFormOf", "IsIdenticalTo", "IsReviewedBy", "Reviews", "IsDerivedFrom", "IsSourceOf", "Describes", "IsDescribedBy", "HasVersion", "IsVersionOf", "Requires", "IsRequiredBy", "Obsoletes", "IsObsoletedBy"]
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
