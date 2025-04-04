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
  "relatedIdentifiers": {
    "type": "array",
    "label": "Related identifiers",
    "tooltip": "The identifiers of other resources related to the resource such as a URN, URI or an ISBN number.",
    "items": {
      "type"
      "object",
      "properties": {
        "relatedID": {
          "type": "string",
          "label": "Related identifier",
          "tooltip": "Please provide the reference/identifier to the related resource."
        },
        "relatedResourceType": {
          "type": "enum",
          "enumValues": [
            "Audiovisual",
            "Book",
            "BookChapter",
            "Collection",
            "ComputationalNotebook",
            "ConferencePaper",
            "ConferenceProceeding",
            "DataPaper",
            "Dataset",
            "Dissertation",
            "Event",
            "Image",
            "InteractiveResource",
            "Journal",
            "JournalArticle",
            "Model",
            "OutputManagementPlan",
            "PeerReview",
            "PhysicalObject",
            "Preprint",
            "Report",
            "Service",
            "Software",
            "Sound",
            "Standard",
            "Text",
            "Workflow",
            "Other"
          ]
        },
        "relatedIDType": {
          "type": "enum",
          "label": "Related Identifier Type",
          "tooltip": "The type of identifier.",
          "enumValues": [
            "ARK",
            "arXiv",
            "bibcode",
            "DOI",
            "EAN13",
            "EISSN",
            "Handle",
            "ISBN",
            "ISSN",
            "ISTC",
            "LISSN",
            "LSID",
            "ORCID",
            "PMID",
            "PURL",
            "UPC",
            "URL",
            "URN",
            "w3id",
            "URI"
          ]
        },
        "relationType": {
          "type": "enum",
          "label": "Relation",
          "tooltip": "The relation type of the described reference.",
          "enumValues": [
            "IsCitedBy",
            "Cites",
            "IsSupplementTo",
            "IsPublishedIn",
            "IsSupplementedBy",
            "IsContinuedBy",
            "Continues",
            "HasMetadata",
            "IsMetadataFor",
            "IsNewVersionOf",
            "IsPreviousVersionOf",
            "IsPartOf",
            "HasPart",
            "IsReferencedBy",
            "References",
            "IsDocumentedBy",
            "Documents",
            "isCompiledBy",
            "Compiles",
            "IsVariantFormOf",
            "IsOriginalFormOf",
            "IsIdenticalTo",
            "IsReviewedBy",
            "Reviews",
            "IsDerivedFrom",
            "IsSourceOf",
            "Describes",
            "IsDescribedBy",
            "HasVersion",
            "IsVersionOf",
            "Requires",
            "IsRequiredBy",
            "Obsoletes",
            "IsObsoletedBy"
          ]
        }
      }
    }
  }
}
```

## Description
### Definition
Is the identifier of a resource to which this item is related in some way (it is derived, it is a subset, etc.).
### Required
optional

### Multiplicity
[0..n]

### RDF Property
[dcterms:relation](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_relation)

### EML Element
_None_

## ISO Mapping

## Provenance
This property can be used to capture provenance information by establishing relationships between the dataset and other datasets. For instance, you can use the property prov:wasDerivedFrom (as defined in [PROV-O](https://www.w3.org/TR/prov-o/#wasDerivedFrom)) or other properties provided by [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/), such as:

- dct:hasPart
- dct:isPartOf
- dct:conformsTo
- dct:isFormatOf
- dct:hasFormat
- dct:isVersionOf
- dct:hasVersion
- dct:replaces
- dct:isReplacedBy
- dct:references
- dct:isReferencedBy
- dct:requires
- dct:isRequiredBy

Additionally, you can leverage other [PROV-O](https://www.w3.org/TR/prov-o/#wasDerivedFrom) properties, such as:

- prov:wasInfluencedBy
- prov:wasQuotedFrom
- prov:wasRevisionOf
- prov:hadPrimarySource
- prov:alternateOf
- prov:specializationOf

These properties collectively enable detailed documentation of relationships and dependencies, fostering better provenance tracking.

## JSON Example

## Ingest Form Mapping

[Back to model](_base.md)
