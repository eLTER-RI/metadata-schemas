"""Facet definitions."""

from invenio_records_resources.services.records.facets import TermsFacet
from oarepo_runtime.i18n import lazy_gettext as _
from oarepo_runtime.services.facets.date import DateTimeFacet

metadata_contributors_affiliation_affiliationIdentifier = TermsFacet(
    field="metadata.contributors.affiliation.affiliationIdentifier",
    label=_("metadata/contributors/affiliation/affiliationIdentifier.label"),
)

metadata_contributors_affiliation_affiliationIdentifierScheme = TermsFacet(
    field="metadata.contributors.affiliation.affiliationIdentifierScheme",
    label=_("metadata/contributors/affiliation/affiliationIdentifierScheme.label"),
)

metadata_contributors_affiliation_name = TermsFacet(
    field="metadata.contributors.affiliation.name",
    label=_("metadata/contributors/affiliation/name.label"),
)

metadata_contributors_affiliation_schemeURI = TermsFacet(
    field="metadata.contributors.affiliation.schemeURI",
    label=_("metadata/contributors/affiliation/schemeURI.label"),
)

metadata_contributors_contributorType = TermsFacet(
    field="metadata.contributors.contributorType",
    label=_("metadata/contributors/contributorType.label"),
)

metadata_contributors_familyName = TermsFacet(
    field="metadata.contributors.familyName",
    label=_("metadata/contributors/familyName.label"),
)

metadata_contributors_givenName = TermsFacet(
    field="metadata.contributors.givenName",
    label=_("metadata/contributors/givenName.label"),
)

metadata_contributors_lang = TermsFacet(
    field="metadata.contributors.lang", label=_("metadata/contributors/lang.label")
)

metadata_contributors_name = TermsFacet(
    field="metadata.contributors.name", label=_("metadata/contributors/name.label")
)

metadata_contributors_nameIdentifiers_nameIdentifier = TermsFacet(
    field="metadata.contributors.nameIdentifiers.nameIdentifier",
    label=_("metadata/contributors/nameIdentifiers/nameIdentifier.label"),
)

metadata_contributors_nameIdentifiers_nameIdentifierScheme = TermsFacet(
    field="metadata.contributors.nameIdentifiers.nameIdentifierScheme",
    label=_("metadata/contributors/nameIdentifiers/nameIdentifierScheme.label"),
)

metadata_contributors_nameIdentifiers_schemeURI = TermsFacet(
    field="metadata.contributors.nameIdentifiers.schemeURI",
    label=_("metadata/contributors/nameIdentifiers/schemeURI.label"),
)

metadata_contributors_nameType = TermsFacet(
    field="metadata.contributors.nameType",
    label=_("metadata/contributors/nameType.label"),
)

metadata_creators_affiliation_affiliationIdentifier = TermsFacet(
    field="metadata.creators.affiliation.affiliationIdentifier",
    label=_("metadata/creators/affiliation/affiliationIdentifier.label"),
)

metadata_creators_affiliation_affiliationIdentifierScheme = TermsFacet(
    field="metadata.creators.affiliation.affiliationIdentifierScheme",
    label=_("metadata/creators/affiliation/affiliationIdentifierScheme.label"),
)

metadata_creators_affiliation_name = TermsFacet(
    field="metadata.creators.affiliation.name",
    label=_("metadata/creators/affiliation/name.label"),
)

metadata_creators_affiliation_schemeURI = TermsFacet(
    field="metadata.creators.affiliation.schemeURI",
    label=_("metadata/creators/affiliation/schemeURI.label"),
)

metadata_creators_familyName = TermsFacet(
    field="metadata.creators.familyName", label=_("metadata/creators/familyName.label")
)

metadata_creators_givenName = TermsFacet(
    field="metadata.creators.givenName", label=_("metadata/creators/givenName.label")
)

metadata_creators_lang = TermsFacet(
    field="metadata.creators.lang", label=_("metadata/creators/lang.label")
)

metadata_creators_name = TermsFacet(
    field="metadata.creators.name", label=_("metadata/creators/name.label")
)

metadata_creators_nameIdentifiers_nameIdentifier = TermsFacet(
    field="metadata.creators.nameIdentifiers.nameIdentifier",
    label=_("metadata/creators/nameIdentifiers/nameIdentifier.label"),
)

metadata_creators_nameIdentifiers_nameIdentifierScheme = TermsFacet(
    field="metadata.creators.nameIdentifiers.nameIdentifierScheme",
    label=_("metadata/creators/nameIdentifiers/nameIdentifierScheme.label"),
)

metadata_creators_nameIdentifiers_schemeURI = TermsFacet(
    field="metadata.creators.nameIdentifiers.schemeURI",
    label=_("metadata/creators/nameIdentifiers/schemeURI.label"),
)

metadata_creators_nameType = TermsFacet(
    field="metadata.creators.nameType", label=_("metadata/creators/nameType.label")
)

metadata_descriptions_descriptionType = TermsFacet(
    field="metadata.descriptions.descriptionType",
    label=_("metadata/descriptions/descriptionType.label"),
)

metadata_descriptions_lang = TermsFacet(
    field="metadata.descriptions.lang", label=_("metadata/descriptions/lang.label")
)

metadata_doi = TermsFacet(field="metadata.doi", label=_("metadata/doi.label"))

metadata_geoLocations_geoLocationBox_eastBoundLongitude = TermsFacet(
    field="metadata.geoLocations.geoLocationBox.eastBoundLongitude",
    label=_("metadata/geoLocations/geoLocationBox/eastBoundLongitude.label"),
)

metadata_geoLocations_geoLocationBox_northBoundLatitude = TermsFacet(
    field="metadata.geoLocations.geoLocationBox.northBoundLatitude",
    label=_("metadata/geoLocations/geoLocationBox/northBoundLatitude.label"),
)

metadata_geoLocations_geoLocationBox_southBoundLatitude = TermsFacet(
    field="metadata.geoLocations.geoLocationBox.southBoundLatitude",
    label=_("metadata/geoLocations/geoLocationBox/southBoundLatitude.label"),
)

metadata_geoLocations_geoLocationBox_westBoundLongitude = TermsFacet(
    field="metadata.geoLocations.geoLocationBox.westBoundLongitude",
    label=_("metadata/geoLocations/geoLocationBox/westBoundLongitude.label"),
)

metadata_geoLocations_geoLocationPlace = TermsFacet(
    field="metadata.geoLocations.geoLocationPlace",
    label=_("metadata/geoLocations/geoLocationPlace.label"),
)

metadata_geoLocations_geoLocationPoint_pointLatitude = TermsFacet(
    field="metadata.geoLocations.geoLocationPoint.pointLatitude",
    label=_("metadata/geoLocations/geoLocationPoint/pointLatitude.label"),
)

metadata_geoLocations_geoLocationPoint_pointLongitude = TermsFacet(
    field="metadata.geoLocations.geoLocationPoint.pointLongitude",
    label=_("metadata/geoLocations/geoLocationPoint/pointLongitude.label"),
)

metadata_geoLocations_geoLocationPolygons_inPolygonPoint_pointLatitude = TermsFacet(
    field="metadata.geoLocations.geoLocationPolygons.inPolygonPoint.pointLatitude",
    label=_(
        "metadata/geoLocations/geoLocationPolygons/inPolygonPoint/pointLatitude.label"
    ),
)

metadata_geoLocations_geoLocationPolygons_inPolygonPoint_pointLongitude = TermsFacet(
    field="metadata.geoLocations.geoLocationPolygons.inPolygonPoint.pointLongitude",
    label=_(
        "metadata/geoLocations/geoLocationPolygons/inPolygonPoint/pointLongitude.label"
    ),
)

metadata_geoLocations_geoLocationPolygons_polygonPoints_pointLatitude = TermsFacet(
    field="metadata.geoLocations.geoLocationPolygons.polygonPoints.pointLatitude",
    label=_(
        "metadata/geoLocations/geoLocationPolygons/polygonPoints/pointLatitude.label"
    ),
)

metadata_geoLocations_geoLocationPolygons_polygonPoints_pointLongitude = TermsFacet(
    field="metadata.geoLocations.geoLocationPolygons.polygonPoints.pointLongitude",
    label=_(
        "metadata/geoLocations/geoLocationPolygons/polygonPoints/pointLongitude.label"
    ),
)

metadata_identifiers_relatedIdentifier = TermsFacet(
    field="metadata.identifiers.relatedIdentifier",
    label=_("metadata/identifiers/relatedIdentifier.label"),
)

metadata_identifiers_relatedIdentifierType = TermsFacet(
    field="metadata.identifiers.relatedIdentifierType",
    label=_("metadata/identifiers/relatedIdentifierType.label"),
)

metadata_identifiers_relatedMetadataScheme = TermsFacet(
    field="metadata.identifiers.relatedMetadataScheme",
    label=_("metadata/identifiers/relatedMetadataScheme.label"),
)

metadata_identifiers_relationType = TermsFacet(
    field="metadata.identifiers.relationType",
    label=_("metadata/identifiers/relationType.label"),
)

metadata_identifiers_resourceTypeGeneral = TermsFacet(
    field="metadata.identifiers.resourceTypeGeneral",
    label=_("metadata/identifiers/resourceTypeGeneral.label"),
)

metadata_identifiers_schemeType = TermsFacet(
    field="metadata.identifiers.schemeType",
    label=_("metadata/identifiers/schemeType.label"),
)

metadata_identifiers_schemeURI = TermsFacet(
    field="metadata.identifiers.schemeURI",
    label=_("metadata/identifiers/schemeURI.label"),
)

metadata_keywords = TermsFacet(
    field="metadata.keywords", label=_("metadata/keywords.label")
)

metadata_language = TermsFacet(
    field="metadata.language", label=_("metadata/language.label")
)

metadata_project = TermsFacet(
    field="metadata.project", label=_("metadata/project.label")
)

metadata_publicationYear = TermsFacet(
    field="metadata.publicationYear", label=_("metadata/publicationYear.label")
)

metadata_resourceTypes_resourceType = TermsFacet(
    field="metadata.resourceTypes.resourceType",
    label=_("metadata/resourceTypes/resourceType.label"),
)

metadata_resourceTypes_resourceTypeGeneral = TermsFacet(
    field="metadata.resourceTypes.resourceTypeGeneral",
    label=_("metadata/resourceTypes/resourceTypeGeneral.label"),
)

metadata_rightsList_lang = TermsFacet(
    field="metadata.rightsList.lang", label=_("metadata/rightsList/lang.label")
)

metadata_rightsList_rights = TermsFacet(
    field="metadata.rightsList.rights", label=_("metadata/rightsList/rights.label")
)

metadata_rightsList_rightsIdentifier = TermsFacet(
    field="metadata.rightsList.rightsIdentifier",
    label=_("metadata/rightsList/rightsIdentifier.label"),
)

metadata_rightsList_rightsIdentifierScheme = TermsFacet(
    field="metadata.rightsList.rightsIdentifierScheme",
    label=_("metadata/rightsList/rightsIdentifierScheme.label"),
)

metadata_rightsList_rightsURI = TermsFacet(
    field="metadata.rightsList.rightsURI",
    label=_("metadata/rightsList/rightsURI.label"),
)

metadata_rightsList_schemeURI = TermsFacet(
    field="metadata.rightsList.schemeURI",
    label=_("metadata/rightsList/schemeURI.label"),
)

metadata_shortName = TermsFacet(
    field="metadata.shortName", label=_("metadata/shortName.label")
)

metadata_taxanomicCoverages_classificationCode = TermsFacet(
    field="metadata.taxanomicCoverages.classificationCode",
    label=_("metadata/taxanomicCoverages/classificationCode.label"),
)

metadata_taxanomicCoverages_lang = TermsFacet(
    field="metadata.taxanomicCoverages.lang",
    label=_("metadata/taxanomicCoverages/lang.label"),
)

metadata_taxanomicCoverages_schemeURI = TermsFacet(
    field="metadata.taxanomicCoverages.schemeURI",
    label=_("metadata/taxanomicCoverages/schemeURI.label"),
)

metadata_taxanomicCoverages_subject = TermsFacet(
    field="metadata.taxanomicCoverages.subject",
    label=_("metadata/taxanomicCoverages/subject.label"),
)

metadata_taxanomicCoverages_subjectScheme = TermsFacet(
    field="metadata.taxanomicCoverages.subjectScheme",
    label=_("metadata/taxanomicCoverages/subjectScheme.label"),
)

metadata_taxanomicCoverages_valueURI = TermsFacet(
    field="metadata.taxanomicCoverages.valueURI",
    label=_("metadata/taxanomicCoverages/valueURI.label"),
)

metadata_temporalCoverages_date = DateTimeFacet(
    field="metadata.temporalCoverages.date",
    label=_("metadata/temporalCoverages/date.label"),
)

metadata_temporalCoverages_dateInformation = TermsFacet(
    field="metadata.temporalCoverages.dateInformation",
    label=_("metadata/temporalCoverages/dateInformation.label"),
)

metadata_temporalCoverages_dateType = TermsFacet(
    field="metadata.temporalCoverages.dateType",
    label=_("metadata/temporalCoverages/dateType.label"),
)


record_status = TermsFacet(field="record_status", label=_("record_status"))

has_draft = TermsFacet(field="has_draft", label=_("has_draft"))
