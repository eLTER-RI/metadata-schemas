import marshmallow as ma
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.validate import OneOf
from oarepo_requests.services.ui_schema import UIRequestsSerializationMixin
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.ui import InvenioUISchema, LocalizedEDTFTime


class LterUISchema(UIRequestsSerializationMixin, InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: LterMetadataUISchema())


class LterMetadataUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorsItemUISchema()))

    creators = ma_fields.List(ma_fields.Nested(lambda: CreatorsItemUISchema()))

    descriptions = ma_fields.List(ma_fields.Nested(lambda: DescriptionsItemUISchema()))

    doi = ma_fields.String()

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: GeoLocationsItemUISchema()))

    identifiers = ma_fields.List(ma_fields.Nested(lambda: IdentifiersItemUISchema()))

    keywords = ma_fields.List(ma_fields.String())

    language = ma_fields.String()

    project = ma_fields.String()

    publicationYear = ma_fields.String()

    resourceTypes = ma_fields.List(
        ma_fields.Nested(lambda: ResourceTypesItemUISchema())
    )

    rightsList = ma_fields.List(ma_fields.Nested(lambda: RightsListItemUISchema()))

    shortName = ma_fields.String()

    taxanomicCoverages = ma_fields.List(
        ma_fields.Nested(lambda: TaxanomicCoveragesItemUISchema())
    )

    temporalCoverages = ma_fields.List(
        ma_fields.Nested(lambda: TemporalCoveragesItemUISchema())
    )


class GeoLocationsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    geoLocationBox = ma_fields.Nested(lambda: GeoLocationBoxUISchema())

    geoLocationPlace = ma_fields.String()

    geoLocationPoint = ma_fields.Nested(lambda: GeoLocationPointUISchema())

    geoLocationPolygons = ma_fields.List(
        ma_fields.Nested(lambda: GeoLocationPolygonsItemUISchema())
    )


class ContributorsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliation = ma_fields.List(ma_fields.Nested(lambda: AffiliationItemUISchema()))

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
        ma_fields.Nested(lambda: NameIdentifiersItemUISchema())
    )

    nameType = ma_fields.String(validate=[OneOf(["Organizational", "Personal"])])


class CreatorsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliation = ma_fields.List(ma_fields.Nested(lambda: AffiliationItemUISchema()))

    familyName = ma_fields.String()

    givenName = ma_fields.String()

    lang = ma_fields.String()

    name = ma_fields.String(required=True)

    nameIdentifiers = ma_fields.List(
        ma_fields.Nested(lambda: NameIdentifiersItemUISchema())
    )

    nameType = ma_fields.String(validate=[OneOf(["Organizational", "Personal"])])


class GeoLocationPolygonsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    inPolygonPoint = ma_fields.Nested(lambda: GeoLocationPointUISchema())

    polygonPoints = ma_fields.List(
        ma_fields.Nested(lambda: GeoLocationPointUISchema()), required=True
    )


class AffiliationItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    affiliationIdentifier = ma_fields.String()

    affiliationIdentifierScheme = ma_fields.String()

    name = ma_fields.String(required=True)

    schemeURI = ma_fields.String()


class DescriptionsItemUISchema(DictOnlySchema):
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


class GeoLocationBoxUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    eastBoundLongitude = ma_fields.Float(required=True)

    northBoundLatitude = ma_fields.Float(required=True)

    southBoundLatitude = ma_fields.Float(required=True)

    westBoundLongitude = ma_fields.Float(required=True)


class GeoLocationPointUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    pointLatitude = ma_fields.Float()

    pointLongitude = ma_fields.Float()


class IdentifiersItemUISchema(DictOnlySchema):
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


class NameIdentifiersItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    nameIdentifier = ma_fields.String(required=True)

    nameIdentifierScheme = ma_fields.String(required=True)

    schemeURI = ma_fields.String()


class ResourceTypesItemUISchema(DictOnlySchema):
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


class RightsListItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    lang = ma_fields.String()

    rights = ma_fields.String()

    rightsIdentifier = ma_fields.String()

    rightsIdentifierScheme = ma_fields.String()

    rightsURI = ma_fields.String()

    schemeURI = ma_fields.String()


class TaxanomicCoveragesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    classificationCode = ma_fields.String()

    lang = ma_fields.String()

    schemeURI = ma_fields.String()

    subject = ma_fields.String(required=True)

    subjectScheme = ma_fields.String()

    valueURI = ma_fields.String()


class TemporalCoveragesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    date = LocalizedEDTFTime(required=True)

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
