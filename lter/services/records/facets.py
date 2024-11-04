"""Facet definitions."""

from invenio_records_resources.services.records.facets import TermsFacet
from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_runtime.services.facets.date import DateTimeFacet
from oarepo_runtime.services.facets.nested_facet import NestedLabeledFacet

external_workflow_id = TermsFacet(
    field="external_workflow.id", label=_("external_workflow/id.label")
)

external_workflow_status = TermsFacet(
    field="external_workflow.status", label=_("external_workflow/status.label")
)

metadata_SOReference_name = TermsFacet(
    field="metadata.SOReference.name", label=_("metadata/SOReference/name.label")
)

metadata_SOReference_url = TermsFacet(
    field="metadata.SOReference.url", label=_("metadata/SOReference/url.label")
)

metadata_additionalMetadata_name = NestedLabeledFacet(
    path="metadata.additionalMetadata",
    nested_facet=TermsFacet(
        field="metadata.additionalMetadata.name",
        label=_("metadata/additionalMetadata/name.label"),
    ),
)

metadata_assetType = TermsFacet(
    field="metadata.assetType", label=_("metadata/assetType.label")
)

metadata_authors_email = TermsFacet(
    field="metadata.authors.email", label=_("metadata/authors/email.label")
)

metadata_authors_familyName = TermsFacet(
    field="metadata.authors.familyName", label=_("metadata/authors/familyName.label")
)

metadata_authors_fullName = TermsFacet(
    field="metadata.authors.fullName", label=_("metadata/authors/fullName.label")
)

metadata_authors_givenName = TermsFacet(
    field="metadata.authors.givenName", label=_("metadata/authors/givenName.label")
)

metadata_authors_ids_id = TermsFacet(
    field="metadata.authors.ids.id", label=_("metadata/authors/ids/id.label")
)

metadata_authors_ids_schema = TermsFacet(
    field="metadata.authors.ids.schema", label=_("metadata/authors/ids/schema.label")
)

metadata_authors_ids_url = TermsFacet(
    field="metadata.authors.ids.url", label=_("metadata/authors/ids/url.label")
)

metadata_contributors_email = TermsFacet(
    field="metadata.contributors.email", label=_("metadata/contributors/email.label")
)

metadata_contributors_familyName = TermsFacet(
    field="metadata.contributors.familyName",
    label=_("metadata/contributors/familyName.label"),
)

metadata_contributors_fullName = TermsFacet(
    field="metadata.contributors.fullName",
    label=_("metadata/contributors/fullName.label"),
)

metadata_contributors_givenName = TermsFacet(
    field="metadata.contributors.givenName",
    label=_("metadata/contributors/givenName.label"),
)

metadata_contributors_ids_id = TermsFacet(
    field="metadata.contributors.ids.id", label=_("metadata/contributors/ids/id.label")
)

metadata_contributors_ids_schema = TermsFacet(
    field="metadata.contributors.ids.schema",
    label=_("metadata/contributors/ids/schema.label"),
)

metadata_contributors_ids_url = TermsFacet(
    field="metadata.contributors.ids.url",
    label=_("metadata/contributors/ids/url.label"),
)

metadata_contributors_type = TermsFacet(
    field="metadata.contributors.type", label=_("metadata/contributors/type.label")
)

metadata_dataLevel = TermsFacet(
    field="metadata.dataLevel", label=_("metadata/dataLevel.label")
)

metadata_datasetIds_identifier = TermsFacet(
    field="metadata.datasetIds.identifier",
    label=_("metadata/datasetIds/identifier.label"),
)

metadata_datasetIds_sourceName = TermsFacet(
    field="metadata.datasetIds.sourceName",
    label=_("metadata/datasetIds/sourceName.label"),
)

metadata_datasetIds_type = TermsFacet(
    field="metadata.datasetIds.type", label=_("metadata/datasetIds/type.label")
)

metadata_datasetIds_url = TermsFacet(
    field="metadata.datasetIds.url", label=_("metadata/datasetIds/url.label")
)

metadata_descriptions_language = TermsFacet(
    field="metadata.descriptions.language",
    label=_("metadata/descriptions/language.label"),
)

metadata_descriptions_type = TermsFacet(
    field="metadata.descriptions.type", label=_("metadata/descriptions/type.label")
)

metadata_ecosystem_PID = TermsFacet(
    field="metadata.ecosystem.PID", label=_("metadata/ecosystem/PID.label")
)

metadata_ecosystem_name = TermsFacet(
    field="metadata.ecosystem.name", label=_("metadata/ecosystem/name.label")
)

metadata_files_format = TermsFacet(
    field="metadata.files.format", label=_("metadata/files/format.label")
)

metadata_files_md5 = TermsFacet(
    field="metadata.files.md5", label=_("metadata/files/md5.label")
)

metadata_files_name = TermsFacet(
    field="metadata.files.name", label=_("metadata/files/name.label")
)

metadata_files_size = TermsFacet(
    field="metadata.files.size", label=_("metadata/files/size.label")
)

metadata_files_sourceUrl = TermsFacet(
    field="metadata.files.sourceUrl", label=_("metadata/files/sourceUrl.label")
)

metadata_geoLocations_EX_BoundingPolygon_inPolygonPoint_latitude = TermsFacet(
    field="metadata.geoLocations.EX_BoundingPolygon.inPolygonPoint.latitude",
    label=_("metadata/geoLocations/EX_BoundingPolygon/inPolygonPoint/latitude.label"),
)

metadata_geoLocations_EX_BoundingPolygon_inPolygonPoint_longitude = TermsFacet(
    field="metadata.geoLocations.EX_BoundingPolygon.inPolygonPoint.longitude",
    label=_("metadata/geoLocations/EX_BoundingPolygon/inPolygonPoint/longitude.label"),
)

metadata_geoLocations_EX_BoundingPolygon_points_latitude = TermsFacet(
    field="metadata.geoLocations.EX_BoundingPolygon.points.latitude",
    label=_("metadata/geoLocations/EX_BoundingPolygon/points/latitude.label"),
)

metadata_geoLocations_EX_BoundingPolygon_points_longitude = TermsFacet(
    field="metadata.geoLocations.EX_BoundingPolygon.points.longitude",
    label=_("metadata/geoLocations/EX_BoundingPolygon/points/longitude.label"),
)

metadata_geoLocations_EX_GeographicBoundingBox_eastBoundLongitude = TermsFacet(
    field="metadata.geoLocations.EX_GeographicBoundingBox.eastBoundLongitude",
    label=_("metadata/geoLocations/EX_GeographicBoundingBox/eastBoundLongitude.label"),
)

metadata_geoLocations_EX_GeographicBoundingBox_northBoundLatitude = TermsFacet(
    field="metadata.geoLocations.EX_GeographicBoundingBox.northBoundLatitude",
    label=_("metadata/geoLocations/EX_GeographicBoundingBox/northBoundLatitude.label"),
)

metadata_geoLocations_EX_GeographicBoundingBox_southBoundLatitude = TermsFacet(
    field="metadata.geoLocations.EX_GeographicBoundingBox.southBoundLatitude",
    label=_("metadata/geoLocations/EX_GeographicBoundingBox/southBoundLatitude.label"),
)

metadata_geoLocations_EX_GeographicBoundingBox_westBoundLongitude = TermsFacet(
    field="metadata.geoLocations.EX_GeographicBoundingBox.westBoundLongitude",
    label=_("metadata/geoLocations/EX_GeographicBoundingBox/westBoundLongitude.label"),
)

metadata_geoLocations_Point_latitude = TermsFacet(
    field="metadata.geoLocations.Point.latitude",
    label=_("metadata/geoLocations/Point/latitude.label"),
)

metadata_geoLocations_Point_longitude = TermsFacet(
    field="metadata.geoLocations.Point.longitude",
    label=_("metadata/geoLocations/Point/longitude.label"),
)

metadata_geoServerInfo_mapData_bytetype = TermsFacet(
    field="metadata.geoServerInfo.mapData.bytetype",
    label=_("metadata/geoServerInfo/mapData/bytetype.label"),
)

metadata_geoServerInfo_mapData_epsgCode = TermsFacet(
    field="metadata.geoServerInfo.mapData.epsgCode",
    label=_("metadata/geoServerInfo/mapData/epsgCode.label"),
)

metadata_geoServerInfo_mapData_features_label = TermsFacet(
    field="metadata.geoServerInfo.mapData.features.label",
    label=_("metadata/geoServerInfo/mapData/features/label.label"),
)

metadata_geoServerInfo_mapData_features_name = TermsFacet(
    field="metadata.geoServerInfo.mapData.features.name",
    label=_("metadata/geoServerInfo/mapData/features/name.label"),
)

metadata_geoServerInfo_mapData_features_style_colour = TermsFacet(
    field="metadata.geoServerInfo.mapData.features.style.colour",
    label=_("metadata/geoServerInfo/mapData/features/style/colour.label"),
)

metadata_geoServerInfo_mapData_path = TermsFacet(
    field="metadata.geoServerInfo.mapData.path",
    label=_("metadata/geoServerInfo/mapData/path.label"),
)

metadata_geoServerInfo_mapData_type = TermsFacet(
    field="metadata.geoServerInfo.mapData.type",
    label=_("metadata/geoServerInfo/mapData/type.label"),
)

metadata_geoServerInfo_serviceType = TermsFacet(
    field="metadata.geoServerInfo.serviceType",
    label=_("metadata/geoServerInfo/serviceType.label"),
)

metadata_keywords_name = TermsFacet(
    field="metadata.keywords.name", label=_("metadata/keywords/name.label")
)

metadata_keywords_url = TermsFacet(
    field="metadata.keywords.url", label=_("metadata/keywords/url.label")
)

metadata_language = TermsFacet(
    field="metadata.language", label=_("metadata/language.label")
)

metadata_licenses_name = TermsFacet(
    field="metadata.licenses.name", label=_("metadata/licenses/name.label")
)

metadata_licenses_url = TermsFacet(
    field="metadata.licenses.url", label=_("metadata/licenses/url.label")
)

metadata_methods_PID = TermsFacet(
    field="metadata.methods.PID", label=_("metadata/methods/PID.label")
)

metadata_methods_steps_title = TermsFacet(
    field="metadata.methods.steps.title", label=_("metadata/methods/steps/title.label")
)

metadata_project_DOI = TermsFacet(
    field="metadata.project.DOI", label=_("metadata/project/DOI.label")
)

metadata_project_PID = TermsFacet(
    field="metadata.project.PID", label=_("metadata/project/PID.label")
)

metadata_project_name = TermsFacet(
    field="metadata.project.name", label=_("metadata/project/name.label")
)

metadata_propertyRights_name = TermsFacet(
    field="metadata.propertyRights.name", label=_("metadata/propertyRights/name.label")
)

metadata_propertyRights_url = TermsFacet(
    field="metadata.propertyRights.url", label=_("metadata/propertyRights/url.label")
)

metadata_publicationDate = DateTimeFacet(
    field="metadata.publicationDate", label=_("metadata/publicationDate.label")
)

metadata_shortNames_language = TermsFacet(
    field="metadata.shortNames.language", label=_("metadata/shortNames/language.label")
)

metadata_siteReference_PID = TermsFacet(
    field="metadata.siteReference.PID", label=_("metadata/siteReference/PID.label")
)

metadata_siteReference_name = TermsFacet(
    field="metadata.siteReference.name", label=_("metadata/siteReference/name.label")
)

metadata_taxonomicCoverages_classification_commonName = TermsFacet(
    field="metadata.taxonomicCoverages.classification.commonName",
    label=_("metadata/taxonomicCoverages/classification/commonName.label"),
)

metadata_taxonomicCoverages_classification_id = TermsFacet(
    field="metadata.taxonomicCoverages.classification.id",
    label=_("metadata/taxonomicCoverages/classification/id.label"),
)

metadata_taxonomicCoverages_classification_rankName = TermsFacet(
    field="metadata.taxonomicCoverages.classification.rankName",
    label=_("metadata/taxonomicCoverages/classification/rankName.label"),
)

metadata_taxonomicCoverages_classification_rankValue = TermsFacet(
    field="metadata.taxonomicCoverages.classification.rankValue",
    label=_("metadata/taxonomicCoverages/classification/rankValue.label"),
)

metadata_temporalCoverages_endDate = DateTimeFacet(
    field="metadata.temporalCoverages.endDate",
    label=_("metadata/temporalCoverages/endDate.label"),
)

metadata_temporalCoverages_startDate = DateTimeFacet(
    field="metadata.temporalCoverages.startDate",
    label=_("metadata/temporalCoverages/startDate.label"),
)

metadata_temporalResolution = TermsFacet(
    field="metadata.temporalResolution", label=_("metadata/temporalResolution.label")
)

metadata_titles_language = TermsFacet(
    field="metadata.titles.language", label=_("metadata/titles/language.label")
)

metadata_version = TermsFacet(
    field="metadata.version", label=_("metadata/version.label")
)

state = TermsFacet(field="state", label=_("Draft State"))


record_status = TermsFacet(field="record_status", label=_("record_status"))

has_draft = TermsFacet(field="has_draft", label=_("has_draft"))
