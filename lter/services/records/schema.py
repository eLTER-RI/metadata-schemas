import marshmallow as ma
from marshmallow import Schema
from marshmallow import fields as ma_fields
from marshmallow.utils import get_value
from marshmallow.validate import OneOf
from marshmallow_utils.fields import SanitizedUnicode
from oarepo_communities.schemas.parent import CommunitiesParentSchema
from oarepo_runtime.services.schema.marshmallow import BaseRecordSchema, DictOnlySchema
from oarepo_runtime.services.schema.validation import validate_date, validate_datetime
from oarepo_workflows.services.records.schema import WorkflowParentSchema


class GeneratedParentSchema(WorkflowParentSchema):
    """"""

    owners = ma.fields.List(ma.fields.Dict(), load_only=True)

    communities = ma_fields.Nested(CommunitiesParentSchema)


class LterSchema(BaseRecordSchema):
    class Meta:
        unknown = ma.RAISE

    externalWorkflow = ma_fields.Nested(lambda: ExternalWorkflowSchema())

    metadata = ma_fields.Nested(lambda: LterMetadataSchema())

    state = ma_fields.String(dump_only=True)

    state_timestamp = ma_fields.String(dump_only=True, validate=[validate_datetime])
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

    SOReference = ma_fields.Nested(lambda: SOReferenceSchema())

    additionalMetadata = ma_fields.List(
        ma_fields.Nested(lambda: AdditionalMetadataItemSchema())
    )

    assetType = ma_fields.String(
        validate=[
            OneOf(
                [
                    "SOATM_027",
                    "SOBIO_017",
                    "SOBIO_096",
                    "SOGEO_001",
                    "SOHYD_004",
                    "SOHYD_168",
                    "NotSpecified",
                ]
            )
        ]
    )

    authors = ma_fields.List(ma_fields.Nested(lambda: AuthorsItemSchema()))

    contributors = ma_fields.List(ma_fields.Nested(lambda: ContributorsItemSchema()))

    dataLevel = ma_fields.Integer(validate=[ma.validate.Range(min=0, max=4)])

    datasetIds = ma_fields.List(ma_fields.Nested(lambda: DatasetIdsItemSchema()))

    descriptions = ma_fields.List(ma_fields.Nested(lambda: DescriptionsItemSchema()))

    ecosystem = ma_fields.Nested(lambda: EcosystemSchema())

    files = ma_fields.List(ma_fields.Nested(lambda: FilesItemSchema()))

    geoLocations = ma_fields.List(ma_fields.Nested(lambda: GeoLocationsItemSchema()))

    geoServerInfo = ma_fields.Nested(lambda: GeoServerInfoSchema())

    keywords = ma_fields.List(ma_fields.Nested(lambda: SOReferenceSchema()))

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

    version = ma_fields.String()


class GeoServerInfoSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    mapData = ma_fields.List(ma_fields.Nested(lambda: MapDataItemSchema()))

    serviceType = ma_fields.String()


class GeoLocationsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    EX_BoundingPolygon = ma_fields.List(
        ma_fields.Nested(lambda: EXBoundingPolygonItemSchema())
    )

    EX_GeographicBoundingBox = ma_fields.Nested(lambda: EXGeographicBoundingBoxSchema())

    EX_GeographicDescription = ma_fields.String()

    Point = ma_fields.Nested(lambda: InPolygonPointSchema())


class MapDataItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    bytetype = ma_fields.Boolean()

    epsgCode = ma_fields.Integer()

    features = ma_fields.Nested(lambda: FeaturesSchema())

    path = ma_fields.String()

    type = ma_fields.String()


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


class EXBoundingPolygonItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    inPolygonPoint = ma_fields.Nested(lambda: InPolygonPointSchema())

    points = ma_fields.List(
        ma_fields.Nested(lambda: InPolygonPointSchema()), required=True
    )


class ExternalWorkflowSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    defaultWorkflowTemplateId = ma_fields.String()

    history = ma_fields.List(
        ma_fields.Nested(lambda: HistoryItemSchema(), dump_only=True)
    )


class FeaturesSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    label = ma_fields.String()

    name = ma_fields.String()

    style = ma_fields.Nested(lambda: StyleSchema())


class MethodsSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    PID = ma_fields.String()

    instrumentationDescription = ma_fields.String()

    qualityControlDescription = ma_fields.String()

    sampling = ma_fields.Nested(lambda: SamplingSchema())

    steps = ma_fields.List(ma_fields.Nested(lambda: StepsItemSchema()))


class TaxonomicCoveragesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    classification = ma_fields.Nested(lambda: ClassificationSchema())

    description = ma_fields.String()


class AdditionalMetadataItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    name = ma_fields.String(required=True)

    value = ma_fields.String(required=True)


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

    identifier = ma_fields.String()

    sourceName = ma_fields.String(required=True)

    type = ma_fields.String()

    url = ma_fields.String()


class DescriptionsItemSchema(DictOnlySchema):
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


class EXGeographicBoundingBoxSchema(DictOnlySchema):
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


class EcosystemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    PID = ma_fields.String()

    name = ma_fields.String()


class FilesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    format = ma_fields.String(required=True)

    md5 = ma_fields.String()

    name = ma_fields.String(required=True)

    size = ma_fields.String()

    sourceUrl = ma_fields.String()


class HistoryItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    date = ma_fields.String(validate=[validate_datetime])

    status = ma_fields.String(
        validate=[OneOf(["Running", "Accepted", "Declined", "Canceled", "Error"])]
    )

    workflowHandle = ma_fields.String()

    workflowTemplateId = ma_fields.String()


class IdsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    _id = ma_fields.String(data_key="id", attribute="id")

    schema = ma_fields.String()

    url = ma_fields.String()


class InPolygonPointSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    latitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-90.0, max=90.0)]
    )

    longitude = ma_fields.Float(
        required=True, validate=[ma.validate.Range(min=-180.0, max=180.0)]
    )


class ProjectSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    DOI = ma_fields.String()

    PID = ma_fields.String()

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

    text = ma_fields.String(required=True)


class StepsItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    description = ma_fields.String()

    title = ma_fields.String(required=True)


class StyleSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    colour = ma_fields.String()


class TemporalCoveragesItemSchema(DictOnlySchema):
    class Meta:
        unknown = ma.RAISE

    endDate = ma_fields.String(required=True, validate=[validate_date("%Y-%m-%d")])

    startDate = ma_fields.String(required=True, validate=[validate_date("%Y-%m-%d")])


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
