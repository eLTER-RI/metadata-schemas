import marshmallow as ma
from edtf import Date as EDTFDate
from edtf import DateAndTime as EDTFDateAndTime
from invenio_drafts_resources.services.records.schema import (
    ParentSchema as InvenioParentSchema,
)
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.utils import get_value
from marshmallow.validate import OneOf
from marshmallow_utils.fields import SanitizedUnicode, TrimmedString
from oarepo_requests.services.schema import RequestsSchemaMixin
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema, DictOnlySchema
from oarepo_runtime.services.schema.validation import CachedMultilayerEDTFValidator


class GeneratedParentSchema(InvenioParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)


class LterSchema(RequestsSchemaMixin, BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: LterMetadataSchema())
    parent = ma.fields.Nested(GeneratedParentSchema)
    files = ma.fields.Nested(
        lambda: FilesOptionsSchema(), load_default={"enabled": True}
    )

    # todo this needs to be generated for [default preview] to work
    def get_attribute(self, obj, attr, default):
        """Override how attributes are retrieved when dumping.

        NOTE: We have to access by attribute because although we are loading
              from an external pure dict, but we are dumping from a data-layer
              object whose fields should be accessed by attributes and not
              keys. Access by key runs into FilesManager key access protection
              and raises.
        """
        if attr == "files":
            return getattr(obj, attr, default)
        else:
            return get_value(obj, attr, default)


class LterMetadataSchema(Schema):
    class Meta:
        unknown = ma.RAISE

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorsItemSchema()))

    creators = ma_fields.List(ma_fields.Nested(lambda: CreatorsItemSchema()))

    descriptions = ma_fields.List(ma_fields.Nested(lambda: DescriptionsItemSchema()))

    doi = ma_fields.String()

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: GeoLocationsItemSchema()))

    identifiers = ma_fields.List(ma_fields.Nested(lambda: IdentifiersItemSchema()))

    keywords = ma_fields.List(ma_fields.String())

    language = ma_fields.String()

    project = ma_fields.String()

    publicationYear = ma_fields.String()

    resourceTypes = ma_fields.List(ma_fields.Nested(lambda: ResourceTypesItemSchema()))

    rightsList = ma_fields.List(ma_fields.Nested(lambda: RightsListItemSchema()))

    shortName = ma_fields.String()

    taxanomicCoverages = ma_fields.List(
        ma_fields.Nested(lambda: TaxanomicCoveragesItemSchema())
    )

    temporalCoverages = ma_fields.List(
        ma_fields.Nested(lambda: TemporalCoveragesItemSchema())
    )


class GeoLocationsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    geoLocationBox = ma_fields.Nested(lambda: GeoLocationBoxSchema())

    geoLocationPlace = ma_fields.String()

    geoLocationPoint = ma_fields.Nested(lambda: GeoLocationPointSchema())

    geoLocationPolygons = ma_fields.List(
        ma_fields.Nested(lambda: GeoLocationPolygonsItemSchema())
    )


class ContributorsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliation = ma_fields.List(ma_fields.Nested(lambda: AffiliationItemSchema()))

    contributorType = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "ContactPerson",
                    "DataCollector",
                    "DataCurator",
                    "DataManager",
                    "Distributor",
                    "Editor",
                    "HostingInstitution",
                    "Producer",
                    "ProjectLeader",
                    "ProjectManager",
                    "ProjectMember",
                    "RegistrationAgency",
                    "RegistrationAuthority",
                    "RelatedPerson",
                    "Researcher",
                    "ResearchGroup",
                    "RightsHolder",
                    "Sponsor",
                    "Supervisor",
                    "WorkPackageLeader",
                    "Other",
                ]
            )
        ],
    )

    familyName = ma_fields.String()

    givenName = ma_fields.String()

    lang = ma_fields.String()

    name = ma_fields.String(required=True)

    nameIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NameIdentifiersItemSchema())
    )

    nameType = ma_fields.String(validate=[OneOf(["Organizational", "Personal"])])


class CreatorsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliation = ma_fields.List(ma_fields.Nested(lambda: AffiliationItemSchema()))

    familyName = ma_fields.String()

    givenName = ma_fields.String()

    lang = ma_fields.String()

    name = ma_fields.String(required=True)

    nameIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NameIdentifiersItemSchema())
    )

    nameType = ma_fields.String(validate=[OneOf(["Organizational", "Personal"])])


class GeoLocationPolygonsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    inPolygonPoint = ma_fields.Nested(lambda: GeoLocationPointSchema())

    polygonPoints = ma_fields.List(
        ma_fields.Nested(lambda: GeoLocationPointSchema()), required=True
    )


class AffiliationItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliationIdentifier = ma_fields.String()

    affiliationIdentifierScheme = ma_fields.String()

    name = ma_fields.String(required=True)

    schemeURI = ma_fields.String()


class DescriptionsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    descriptionType = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Abstract",
                    "Methods",
                    "SeriesInformation",
                    "TableOfContents",
                    "TechnicalInfo",
                    "Other",
                ]
            )
        ],
    )

    lang = ma_fields.String()


class GeoLocationBoxSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    eastBoundLongitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-180.0, max=180.0)]
    )

    northBoundLatitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-90.0, max=90.0)]
    )

    southBoundLatitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-90.0, max=90.0)]
    )

    westBoundLongitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-180.0, max=180.0)]
    )


class GeoLocationPointSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    pointLatitude = ma_fields.Float(validate=[ma.validate.Range(min=-90.0, max=90.0)])

    pointLongitude = ma_fields.Float(
        validate=[ma.validate.Range(min=-180.0, max=180.0)]
    )


class IdentifiersItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    relatedIdentifier = ma_fields.String()

    relatedIdentifierType = ma_fields.String(
        validate=[
            OneOf(
                [
                    "ARK",
                    "arXiv",
                    "bibcode",
                    "DOI",
                    "EAN13",
                    "EISSN",
                    "Handle",
                    "IGSN",
                    "ISBN",
                    "ISSN",
                    "ISTC",
                    "LISSN",
                    "LSID",
                    "PMID",
                    "PURL",
                    "UPC",
                    "URL",
                    "URN",
                    "w3id",
                ]
            )
        ]
    )

    relatedMetadataScheme = ma_fields.String()

    relationType = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "IsCitedBy",
                    "Cites",
                    "IsCollectedBy",
                    "Collects",
                    "IsSupplementTo",
                    "IsSupplementedBy",
                    "IsContinuedBy",
                    "Continues",
                    "IsDescribedBy",
                    "Describes",
                    "HasMetadata",
                    "IsMetadataFor",
                    "HasVersion",
                    "IsVersionOf",
                    "IsNewVersionOf",
                    "IsPartOf",
                    "IsPreviousVersionOf",
                    "IsPublishedIn",
                    "HasPart",
                    "IsReferencedBy",
                    "References",
                    "IsDocumentedBy",
                    "Documents",
                    "IsCompiledBy",
                    "Compiles",
                    "IsVariantFormOf",
                    "IsOriginalFormOf",
                    "IsIdenticalTo",
                    "IsReviewedBy",
                    "Reviews",
                    "IsDerivedFrom",
                    "IsSourceOf",
                    "IsRequiredBy",
                    "Requires",
                    "IsObsoletedBy",
                    "Obsoletes",
                ]
            )
        ],
    )

    resourceTypeGeneral = ma_fields.String(
        validate=[
            OneOf(
                [
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
                    "Instrument",
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
                    "StudyRegistration",
                    "Text",
                    "Workflow",
                    "Other",
                ]
            )
        ]
    )

    schemeType = ma_fields.String()

    schemeURI = ma_fields.String()


class NameIdentifiersItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    nameIdentifier = ma_fields.String(required=True)

    nameIdentifierScheme = ma_fields.String(required=True)

    schemeURI = ma_fields.String()


class ResourceTypesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    resourceType = ma_fields.String()

    resourceTypeGeneral = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
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
                    "Instrument",
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
                    "StudyRegistration",
                    "Text",
                    "Workflow",
                    "Other",
                ]
            )
        ],
    )


class RightsListItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    lang = ma_fields.String()

    rights = ma_fields.String()

    rightsIdentifier = ma_fields.String()

    rightsIdentifierScheme = ma_fields.String()

    rightsURI = ma_fields.String()

    schemeURI = ma_fields.String()


class TaxanomicCoveragesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    classificationCode = ma_fields.String()

    lang = ma_fields.String()

    schemeURI = ma_fields.String()

    subject = ma_fields.String(required=True)

    subjectScheme = ma_fields.String()

    valueURI = ma_fields.String()


class TemporalCoveragesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    date = TrimmedString(
        required=True,
        validate=[
            CachedMultilayerEDTFValidator(
                types=(
                    EDTFDateAndTime,
                    EDTFDate,
                )
            )
        ],
    )

    dateInformation = ma_fields.String()

    dateType = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Accepted",
                    "Available",
                    "Copyrighted",
                    "Collected",
                    "Created",
                    "Issued",
                    "Submitted",
                    "Updated",
                    "Valid",
                    "Withdrawn",
                    "Other",
                ]
            )
        ],
    )


class FilesOptionsSchema(ma.Schema):
    """Basic files options schema class."""

    enabled = ma.fields.Bool(missing=True)
    # allow unsetting
    default_preview = SanitizedUnicode(allow_none=True)

    def get_attribute(self, obj, attr, default):
        """Override how attributes are retrieved when dumping.

        NOTE: We have to access by attribute because although we are loading
              from an external pure dict, but we are dumping from a data-layer
              object whose fields should be accessed by attributes and not
              keys. Access by key runs into FilesManager key access protection
              and raises.
        """
        value = getattr(obj, attr, default)

        if attr == "default_preview" and not value:
            return default

        return value
