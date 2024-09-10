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

    substring_search_field = ma_fields.String()


class LterMetadataUISchema(Schema):
    class Meta:
        unknown = ma.RAISE

    SOReference = ma_fields.Nested(lambda: SOReferenceUISchema())

    additionalMetadata = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalMetadataItemUISchema())
    )

    authors = ma_fields.List(ma_fields.Nested(lambda: AuthorsItemUISchema()))

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorsItemUISchema()))

    dataLevel = ma_fields.Integer()

    datasetIds = ma_fields.List(ma_fields.Nested(lambda: DatasetIdsItemUISchema()))

    descriptions = ma_fields.List(ma_fields.Nested(lambda: DescriptionsItemUISchema()))

    ecosystem = ma_fields.Nested(lambda: EcosystemUISchema())

    files = ma_fields.List(ma_fields.Nested(lambda: FilesItemUISchema()))

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: GeoLocationsItemUISchema()))

    geoServerInfo = ma_fields.Nested(lambda: GeoServerInfoUISchema())

    keywords = ma_fields.List(ma_fields.Nested(lambda: SOReferenceUISchema()))

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


class GeoServerInfoUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    mapData = ma_fields.List(ma_fields.Nested(lambda: MapDataItemUISchema()))

    serviceType = ma_fields.String()


class GeoLocationsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    EX_BoundingPolygon = ma_fields.List(
        ma_fields.Nested(lambda: EXBoundingPolygonItemUISchema())
    )

    EX_GeographicBoundingBox = ma_fields.Nested(
        lambda: EXGeographicBoundingBoxUISchema()
    )

    EX_GeographicDescription = ma_fields.String()

    Point = ma_fields.Nested(lambda: InPolygonPointUISchema())


class MapDataItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    bytetype = ma_fields.Boolean()

    epsgCode = ma_fields.Integer()

    features = ma_fields.Nested(lambda: FeaturesUISchema())

    path = ma_fields.String()

    type = ma_fields.String()


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


class EXBoundingPolygonItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    inPolygonPoint = ma_fields.Nested(lambda: InPolygonPointUISchema())

    points = ma_fields.List(
        ma_fields.Nested(lambda: InPolygonPointUISchema()), required=True
    )


class FeaturesUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    label = ma_fields.String()

    name = ma_fields.String()

    style = ma_fields.Nested(lambda: StyleUISchema())


class MethodsUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    PID = ma_fields.String()

    instrumentationDescription = ma_fields.String()

    qualityControlDescription = ma_fields.String()

    sampling = ma_fields.Nested(lambda: SamplingUISchema())

    steps = ma_fields.List(ma_fields.Nested(lambda: StepsItemUISchema()))


class TaxonomicCoveragesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    classification = ma_fields.Nested(lambda: ClassificationUISchema())

    description = ma_fields.String()


class AdditionalMetadataItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    name = ma_fields.String(required=True)

    value = ma_fields.String(required=True)


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

    identifier = ma_fields.String()

    sourceName = ma_fields.String(required=True)

    type = ma_fields.String()

    url = ma_fields.String()


class DescriptionsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String(required=True)

    language = ma_fields.String()

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


class EXGeographicBoundingBoxUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    eastBoundLongitude = ma_fields.Float(required=True)

    northBoundLatitude = ma_fields.Float(required=True)

    southBoundLatitude = ma_fields.Float(required=True)

    westBoundLongitude = ma_fields.Float(required=True)


class EcosystemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    PID = ma_fields.String()

    name = ma_fields.String()


class FilesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    format = ma_fields.String(required=True)

    md5 = ma_fields.String()

    name = ma_fields.String(required=True)

    size = ma_fields.Integer()

    sourceUrl = ma_fields.String()


class IdsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    schema = ma_fields.String()

    url = ma_fields.String()


class InPolygonPointUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    latitude = ma_fields.Float(required=True)

    longitude = ma_fields.Float(required=True)


class ProjectUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    DOI = ma_fields.String()

    PID = ma_fields.String()

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

    text = ma_fields.String(required=True)


class StepsItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String()

    title = ma_fields.String(required=True)


class StyleUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    colour = ma_fields.String()


class TemporalCoveragesItemUISchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    endDate = LocalizedDate(required=True)

    startDate = LocalizedDate(required=True)
