import marshmallow as ma
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.validate import OneOf
from oarepo_requests.services.ui_schema import UIRequestsSerializationMixin
from oarepo_runtime.services.schema.marshmallow import DictOnlySchema
from oarepo_runtime.services.schema.ui import InvenioUISchema, LocalizedDate


class LterUISchema(UIRequestsSerializationMixin, InvenioUISchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: LterMetadataUISchema())


class LterMetadataUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    SOReference = ma_fields.Nested(lambda: SOReferenceUISchema())

    authors = ma_fields.List(ma_fields.Nested(lambda: AuthorsItemUISchema()))

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorsItemUISchema()))

    dataLevel = ma_fields.Integer()

    datasetIds = ma_fields.List(ma_fields.Nested(lambda: DatasetIdsItemUISchema()))

    descriptions = ma_fields.List(ma_fields.Nested(lambda: DescriptionsItemUISchema()))

    ecosystem = ma_fields.Nested(lambda: EcosystemUISchema())

    files = ma_fields.List(ma_fields.Nested(lambda: FilesItemUISchema()))

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: GeoLocationsItemUISchema()))

    keywords = ma_fields.List(ma_fields.String())

    language = ma_fields.String()

    licenses = ma_fields.List(ma_fields.Nested(lambda: SOReferenceUISchema()))

    methods = ma_fields.Nested(lambda: MethodsUISchema())

    project = ma_fields.Nested(lambda: ProjectUISchema())

    propertyRights = ma_fields.List(ma_fields.Nested(lambda: SOReferenceUISchema()))

    publicationDate = LocalizedDate()

    shortNames = ma_fields.List(ma_fields.Nested(lambda: ShortNamesItemUISchema()))

    siteReference = ma_fields.List(ma_fields.Nested(lambda: EcosystemUISchema()))

    taxonomicCoverages = ma_fields.List(
        ma_fields.Nested(lambda: TaxonomicCoveragesItemUISchema())
    )

    temporalCoverages = ma_fields.List(
        ma_fields.Nested(lambda: TemporalCoveragesItemUISchema())
    )

    temporalResolution = ma_fields.Integer()

    titles = ma_fields.List(ma_fields.Nested(lambda: ShortNamesItemUISchema()))


class GeoLocationsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    box = ma_fields.Nested(lambda: BoxUISchema())

    description = ma_fields.String()

    point = ma_fields.Nested(lambda: PointUISchema())

    polygon = ma_fields.List(ma_fields.Nested(lambda: PolygonItemUISchema()))


class AuthorsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    email = ma_fields.String()

    familyName = ma_fields.String()

    fullName = ma_fields.String()

    givenName = ma_fields.String()

    ids = ma_fields.List(ma_fields.Nested(lambda: IdsItemUISchema()))


class ContributorsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    email = ma_fields.String()

    familyName = ma_fields.String()

    fullName = ma_fields.String()

    givenName = ma_fields.String()

    ids = ma_fields.List(ma_fields.Nested(lambda: IdsItemUISchema()))

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "ContactPerson",
                    "DataCollector",
                    "DataCurator",
                    "DataManager",
                    "MetadataProvider",
                    "Producer",
                    "ProjectLeader",
                    "ProjectManager",
                    "ProjectMember",
                    "RegistrationAuthority",
                    "RelatedPerson",
                    "Researcher",
                    "ResearchGroup",
                    "Other",
                ]
            )
        ],
    )


class MethodsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    PID = ma_fields.String()

    instrumentationDescription = ma_fields.String()

    qualityControlDescription = ma_fields.String()

    sampling = ma_fields.Nested(lambda: SamplingUISchema())

    steps = ma_fields.List(ma_fields.Nested(lambda: StepsItemUISchema()))


class PolygonItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    inPolygonPoint = ma_fields.Nested(lambda: PointUISchema())

    points = ma_fields.List(ma_fields.Nested(lambda: PointUISchema()), required=True)


class TaxonomicCoveragesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    classification = ma_fields.Nested(lambda: ClassificationUISchema())

    description = ma_fields.String()


class BoxUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    eastLongitude = ma_fields.Float(required=True)

    northLatitude = ma_fields.Float(required=True)

    southLatitude = ma_fields.Float(required=True)

    westLongitude = ma_fields.Float(required=True)


class ClassificationUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    commonName = ma_fields.String()

    rankName = ma_fields.String()

    rankValue = ma_fields.String()


class DatasetIdsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    identifier = ma_fields.String(required=True)

    source = ma_fields.String()

    type = ma_fields.String(required=True)

    url = ma_fields.String()


class DescriptionsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    language = ma_fields.String(required=True)

    type = ma_fields.String(
        required=True,
        validate=[
            OneOf(
                [
                    "Abstract",
                    "AdditionalInfo",
                    "Methods",
                    "SeriesInformation",
                    "TableOfContents",
                    "TechnicalInfo",
                    "Other",
                ]
            )
        ],
    )


class EcosystemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    PID = ma_fields.String()

    name = ma_fields.String()


class FilesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    format = ma_fields.String()

    md5 = ma_fields.String()

    name = ma_fields.String()

    size = ma_fields.Integer()

    sourceUrl = ma_fields.String()


class IdsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    schema = ma_fields.String(required=True)

    url = ma_fields.String()


class PointUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    latitude = ma_fields.Float()

    longitude = ma_fields.Float()


class ProjectUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    DOI = ma_fields.String()

    PID = ma_fields.String(required=True)

    name = ma_fields.String(required=True)


class SOReferenceUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    name = ma_fields.String()

    url = ma_fields.String()


class SamplingUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    samplingDescription = ma_fields.String()

    studyDescription = ma_fields.String()


class ShortNamesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    language = ma_fields.String()

    text = ma_fields.String()


class StepsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String()

    title = ma_fields.String(required=True)


class TemporalCoveragesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    endDate = LocalizedDate()

    startDate = LocalizedDate()
