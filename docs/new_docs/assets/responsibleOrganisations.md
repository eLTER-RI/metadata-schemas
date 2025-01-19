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
  "responsibleOrganisations": {
    "type" "array",
    "label": "Responsible Organisations",
    "definition": "Responsible organisation and contact information owning the resource.",
    "tooltip": "Responsible organisation and contact information owning the resource.",
    "required": true,
    "items": {
      "type": "object",
      "properties": {
        "organisation_name": {
          "type": "string",
          "label": "Organisation name",
          "tooltip": "Provide the name of the responsible organisation"
        },
        "email": {
          "type": "string",
          "label": "Contact information",
          "tooltip": "Contact email for the resource."
        },
        "organisation_identifier": {
            "type": "string",
            "label": "Organisation ID",
            "placeholder": "https://ror.org/000h6jb29",
            "tooltip": "Provide identifier (e.g. ROR) for the organisation, e.g. https://ror.org/",
            "required": false
          }
        }
      }
    }
  }
```

## Description
### Definition
Responsible organisation and contact information owning the resource.
## Discussion
The responsibleOrganisation is defining the organisation responsible and owning the resource (e.g. dataset) including the provision of an email as contact information for the resource. In the contributor there is also a role "contact point" which is not clear at the moment if that is used.
### Required
mandatory

### Multiplicity
[1..n]

### RDF Property
[dcterms:publisher](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_publisher)

### EML URL
[metadataProvider](https://eml.ecoinformatics.org/schema/eml-resource_xsd.html#ResourceGroup_metadataProvider)

## ISO Mapping

## Provenance
This property can be used to capture provenance information by establishing relationships between the dataset and the metadata provider using the property: [prov:wasAttributedTo](https://www.w3.org/TR/prov-o/#wasAttributedTo)

## JSON Example

## Ingest Form Mapping

[Back to model](_base.md)
