import marshmallow as ma
from invenio_drafts_resources.services.records.schema import (
    ParentSchema as InvenioParentSchema,
)
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.validate import OneOf
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema, DictOnlySchema
from oarepo_runtime.services.schema.validation import validate_date


class GeneratedParentSchema(InvenioParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)


class LterSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    metadata = ma_fields.Nested(lambda: LterMetadataSchema())
    parent = ma.fields.Nested(GeneratedParentSchema)


class LterMetadataSchema(Schema):
    class Meta:
        unknown = ma.RAISE

    SOReference = ma_fields.Nested(lambda: SOReferenceSchema())

    authors = ma_fields.List(ma_fields.Nested(lambda: AuthorsItemSchema()))

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorsItemSchema()))

    dataLevel = ma_fields.Integer(validate=[ma.validate.Range(min=0, max=4)])

    datasetIds = ma_fields.List(ma_fields.Nested(lambda: DatasetIdsItemSchema()))

    descriptions = ma_fields.List(ma_fields.Nested(lambda: DescriptionsItemSchema()))

    ecosystem = ma_fields.Nested(lambda: EcosystemSchema())

    files = ma_fields.List(ma_fields.Nested(lambda: FilesItemSchema()))

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: GeoLocationsItemSchema()))

    keywords = ma_fields.List(ma_fields.String())

    language = ma_fields.String()

    licenses = ma_fields.List(ma_fields.Nested(lambda: SOReferenceSchema()))

    methods = ma_fields.Nested(lambda: MethodsSchema())

    project = ma_fields.Nested(lambda: ProjectSchema())

    propertyRights = ma_fields.List(ma_fields.Nested(lambda: SOReferenceSchema()))

    publicationDate = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    shortNames = ma_fields.List(ma_fields.Nested(lambda: ShortNamesItemSchema()))

    siteReference = ma_fields.List(ma_fields.Nested(lambda: EcosystemSchema()))

    taxonomicCoverages = ma_fields.List(
        ma_fields.Nested(lambda: TaxonomicCoveragesItemSchema())
    )

    temporalCoverages = ma_fields.List(
        ma_fields.Nested(lambda: TemporalCoveragesItemSchema())
    )

    temporalResolution = ma_fields.Integer(validate=[ma.validate.Range(min=0)])

    titles = ma_fields.List(ma_fields.Nested(lambda: ShortNamesItemSchema()))


class GeoLocationsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    box = ma_fields.Nested(lambda: BoxSchema())

    description = ma_fields.String()

    point = ma_fields.Nested(lambda: PointSchema())

    polygon = ma_fields.List(ma_fields.Nested(lambda: PolygonItemSchema()))


class AuthorsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    email = ma_fields.String()

    familyName = ma_fields.String()

    fullName = ma_fields.String()

    givenName = ma_fields.String()

    ids = ma_fields.List(ma_fields.Nested(lambda: IdsItemSchema()))


class ContributorsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    email = ma_fields.String()

    familyName = ma_fields.String()

    fullName = ma_fields.String()

    givenName = ma_fields.String()

    ids = ma_fields.List(ma_fields.Nested(lambda: IdsItemSchema()))

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


class MethodsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    PID = ma_fields.String()

    instrumentationDescription = ma_fields.String()

    qualityControlDescription = ma_fields.String()

    sampling = ma_fields.Nested(lambda: SamplingSchema())

    steps = ma_fields.List(ma_fields.Nested(lambda: StepsItemSchema()))


class PolygonItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    inPolygonPoint = ma_fields.Nested(lambda: PointSchema())

    points = ma_fields.List(ma_fields.Nested(lambda: PointSchema()), required=True)


class TaxonomicCoveragesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    classification = ma_fields.Nested(lambda: ClassificationSchema())

    description = ma_fields.String()


class BoxSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    eastLongitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-180.0, max=180.0)]
    )

    northLatitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-90.0, max=90.0)]
    )

    southLatitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-90.0, max=90.0)]
    )

    westLongitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-180.0, max=180.0)]
    )


class ClassificationSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    commonName = ma_fields.String()

    rankName = ma_fields.String()

    rankValue = ma_fields.String()


class DatasetIdsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    identifier = ma_fields.String(required=True)

    source = ma_fields.String()

    type = ma_fields.String(required=True)

    url = ma_fields.String()


class DescriptionsItemSchema(DictOnlySchema):
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


class EcosystemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    PID = ma_fields.String()

    name = ma_fields.String()


class FilesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    format = ma_fields.String()

    md5 = ma_fields.String()

    name = ma_fields.String()

    size = ma_fields.Integer()

    sourceUrl = ma_fields.String()


class IdsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(required=True, data_key="id", attribute="id")

    schema = ma_fields.String(required=True)

    url = ma_fields.String()


class PointSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    latitude = ma_fields.Float(validate=[ma.validate.Range(min=-90.0, max=90.0)])

    longitude = ma_fields.Float(validate=[ma.validate.Range(min=-180.0, max=180.0)])


class ProjectSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    DOI = ma_fields.String()

    PID = ma_fields.String(required=True)

    name = ma_fields.String(required=True)


class SOReferenceSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    name = ma_fields.String()

    url = ma_fields.String()


class SamplingSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    samplingDescription = ma_fields.String()

    studyDescription = ma_fields.String()


class ShortNamesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    language = ma_fields.String()

    text = ma_fields.String()


class StepsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String()

    title = ma_fields.String(required=True)


class TemporalCoveragesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    endDate = ma_fields.String(validate=[validate_date("%Y-%m-%d")])

    startDate = ma_fields.String(validate=[validate_date("%Y-%m-%d")])
