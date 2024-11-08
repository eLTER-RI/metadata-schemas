import json
from datetime import datetime
import pytz
from lxml import etree

language_table = {
    "albanian": "alb",
    "armenian": "arm",
    "basque": "baq",
    "belarusian": "bel",
    "bosnian": "bos",
    "breton": "bre",
    "bulgarian": "bul",
    "catalan": "cat",
    "corsican": "cos",
    "croatian": "hrv",
    "czech": "cze",
    "danish": "dan",
    "dutch": "dut",
    "english": "eng",
    "estonian": "est",
    "faroese": "fao",
    "finnish": "fin",
    "french": "fre",
    "galician": "glg",
    "georgian": "geo",
    "german": "ger",
    "greek": "gre",
    "hungarian": "hun",
    "icelandic": "ice",
    "irish": "gle",
    "italian": "ita",
    "latvian": "lav",
    "lithuanian": "lit",
    "luxembourgish": "ltz",
    "macedonian": "mac",
    "maltese": "mlt",
    "moldavian": "mol",
    "montenegrin": "cnr",
    "norwegian": "nor",
    "polish": "pol",
    "portuguese": "por",
    "romanian": "rum",
    "russian": "rus",
    "sami": "sme",
    "serbian": "srp",
    "slovak": "slo",
    "slovenian": "slv",
    "spanish": "spa",
    "swedish": "swe",
    "turkish": "tur",
    "ukrainian": "ukr",
    "welsh": "wel",
}


def get_current_datetime():
    tz = pytz.timezone('Europe/London')
    now = datetime.now(tz)
    return now.isoformat()


def create_element(tag, text, nsmap=None):
    element = etree.Element(tag, nsmap=nsmap)
    element.text = text
    return element


def create_root_element(nsmap):
    root = etree.Element("{http://www.isotc211.org/2005/gmd}MD_Metadata", nsmap=nsmap)
    root.set("{http://www.w3.org/2001/XMLSchema-instance}schemaLocation",
             "http://www.isotc211.org/2005/gmd http://schemas.opengis.net/iso/19139/20060504/gmd/gmd.xsd http://www.w3.org/1999/xlink http://www.isotc211.org/2005/gmx http://www.opengis.net/gml")
    return root


def add_file_identifier(root, file_id, nsmap):
    file_identifier = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}fileIdentifier")
    file_identifier.append(create_element("{http://www.isotc211.org/2005/gco}CharacterString", file_id, nsmap))


def add_language(root, language, nsmap):
    language_element = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}language")
    language_element.append(create_element("{http://www.isotc211.org/2005/gco}CharacterString", language, nsmap))


def add_language_code(root, code_list_value, language_text):
    language_element = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}language")
    language_code = etree.SubElement(language_element, "{http://www.isotc211.org/2005/gmd}LanguageCode",
                                     codeList="http://www.loc.gov/standards/iso639-2/",
                                     codeListValue=code_list_value)
    language_code.text = language_text


def add_character_set(root):
    character_set = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}characterSet")
    character_set_code = etree.SubElement(character_set, "{http://www.isotc211.org/2005/gmd}MD_CharacterSetCode",
                                          codeList="http://www.isotc211.org/2005/resources/codeList.xml#MD_CharacterSetCode",
                                          codeListValue="utf8")
    character_set_code.text = "utf8"


def add_hierarchy_level(root):
    hierarchy_level = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}hierarchyLevel")
    scope_code = etree.SubElement(hierarchy_level, "{http://www.isotc211.org/2005/gmd}MD_ScopeCode",
                                  codeList="http://www.isotc211.org/2005/resources/codeList.xml#MD_ScopeCode",
                                  codeListValue="dataset")
    scope_code.text = "dataset"


def add_date_stamp(root, date_time):
    date_stamp = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}dateStamp")
    date_time_element = etree.SubElement(date_stamp, "{http://www.isotc211.org/2005/gco}DateTime")
    date_time_element.text = date_time


def add_authors(root, authors, nsmap):
    for author in authors:
        contact = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}contact")
        ci_responsible_party = etree.SubElement(contact, "{http://www.isotc211.org/2005/gmd}CI_ResponsibleParty")

        individual_name = etree.SubElement(ci_responsible_party, "{http://www.isotc211.org/2005/gmd}individualName")
        individual_name.append(
            create_element("{http://www.isotc211.org/2005/gco}CharacterString",
                           author.get('fullName', f'{author.get('givenName', '')} {author.get('familyName', '')}'),
                           nsmap))

        contact_info = etree.SubElement(ci_responsible_party, "{http://www.isotc211.org/2005/gmd}contactInfo")
        ci_contact = etree.SubElement(contact_info, "{http://www.isotc211.org/2005/gmd}CI_Contact")
        address = etree.SubElement(ci_contact, "{http://www.isotc211.org/2005/gmd}address")
        ci_address = etree.SubElement(address, "{http://www.isotc211.org/2005/gmd}CI_Address")
        electronic_mail_address = etree.SubElement(ci_address,
                                                   "{http://www.isotc211.org/2005/gmd}electronicMailAddress")
        electronic_mail_address.append(
            create_element("{http://www.isotc211.org/2005/gco}CharacterString", author.get('email', 'NoEmail'), nsmap))

        role = etree.SubElement(ci_responsible_party, "{http://www.isotc211.org/2005/gmd}role")
        ci_role_code = etree.SubElement(role, "{http://www.isotc211.org/2005/gmd}CI_RoleCode",
                                        codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_RoleCode",
                                        codeListValue="pointOfContact")
        ci_role_code.text = "pointOfContact"


def add_license_info(root, licenses):
    if len(licenses) > 0:
        resource_constraints = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}resourceConstraints")

        md_legal_constraints = etree.SubElement(resource_constraints,
                                                "{http://www.isotc211.org/2005/gmd}MD_LegalConstraints")

        use_constraints = etree.SubElement(md_legal_constraints, "{http://www.isotc211.org/2005/gmd}useConstraints")
        etree.SubElement(use_constraints, "{http://www.isotc211.org/2005/gmd}MD_RestrictionCode",
                         {
                             'codeList': "http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#MD_RestrictionCode",
                             'codeListValue': "otherRestrictions"
                         })

        for ele_license in licenses:
            other_constraints = etree.SubElement(md_legal_constraints,
                                                 "{http://www.isotc211.org/2005/gmd}otherConstraints")
            anchor = etree.SubElement(other_constraints, "{http://www.isotc211.org/2005/gmx}Anchor", {
                '{http://www.w3.org/1999/xlink}href': ele_license.get('url', 'Error')
            })
            anchor.text = ele_license.get('name', 'NoName')


def add_temporal_extent_info(root, temporal_coverage):
    if len(temporal_coverage) > 0:
        md_data_identification = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}MD_DataIdentification")
        extent = etree.SubElement(md_data_identification, "{http://www.isotc211.org/2005/gmd}extent")

        ex_extent = etree.SubElement(extent, "{http://www.isotc211.org/2005/gmd}EX_Extent")

        for coverage in temporal_coverage:
            temporal_element = etree.SubElement(ex_extent, "{http://www.isotc211.org/2005/gmd}temporalElement")
            ex_temporal_extent = etree.SubElement(temporal_element,
                                                  "{http://www.isotc211.org/2005/gmd}EX_TemporalExtent")
            gmd_extent = etree.SubElement(ex_temporal_extent, "{http://www.isotc211.org/2005/gmd}extent")

            time_period = etree.SubElement(gmd_extent, "{http://www.opengis.net/gml}TimePeriod")
            begin_position = etree.SubElement(time_period, "{http://www.opengis.net/gml}beginPosition")
            begin_position.text = coverage.get('startDate')
            end_position = etree.SubElement(time_period, "{http://www.opengis.net/gml}endPosition")
            end_position.text = coverage.get('endDate')


def add_identification_info(root, metadata, nsmap):
    identification_info = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}identificationInfo")
    data_identification = etree.SubElement(identification_info,
                                           "{http://www.isotc211.org/2005/gmd}MD_DataIdentification")

    citation = etree.SubElement(data_identification, "{http://www.isotc211.org/2005/gmd}citation")
    ci_citation = etree.SubElement(citation, "{http://www.isotc211.org/2005/gmd}CI_Citation")
    title = etree.SubElement(ci_citation, "{http://www.isotc211.org/2005/gmd}title")
    title.append(
        create_element("{http://www.isotc211.org/2005/gco}CharacterString",
                       metadata.get('titles', [{"text": 'No title'}])[0]['text'], nsmap))

    date = etree.SubElement(ci_citation, "{http://www.isotc211.org/2005/gmd}date")
    ci_date = etree.SubElement(date, "{http://www.isotc211.org/2005/gmd}CI_Date")
    date_element = etree.SubElement(ci_date, "{http://www.isotc211.org/2005/gmd}date")
    date_element.append(create_element("{http://www.isotc211.org/2005/gco}Date", metadata['publicationDate'], nsmap))
    date_type = etree.SubElement(ci_date, "{http://www.isotc211.org/2005/gmd}dateType")
    ci_date_type_code = etree.SubElement(date_type, "{http://www.isotc211.org/2005/gmd}CI_DateTypeCode",
                                         codeList="http://www.isotc211.org/2005/resources/codeList.xml#CI_DateTypeCode",
                                         codeListValue="publication")
    ci_date_type_code.text = "publication"

    abstract = etree.SubElement(data_identification, "{http://www.isotc211.org/2005/gmd}abstract")
    abstract.append(create_element("{http://www.isotc211.org/2005/gco}CharacterString",
                                   metadata['descriptions'][0]['description'], nsmap))

    descriptive_keywords = etree.SubElement(data_identification,
                                            "{http://www.isotc211.org/2005/gmd}descriptiveKeywords")
    md_keywords = etree.SubElement(descriptive_keywords, "{http://www.isotc211.org/2005/gmd}MD_Keywords")

    keywords = metadata.get('keywords', [])
    for keyword in keywords:
        keyword_element = etree.SubElement(md_keywords, "{http://www.isotc211.org/2005/gmd}keyword")
        keyword_element.append(
            create_element("{http://www.isotc211.org/2005/gco}CharacterString", keyword['name'], nsmap))

    sites = metadata.get('siteReference', [])
    for site in sites:
        keyword_element = etree.SubElement(md_keywords, "{http://www.isotc211.org/2005/gmd}keyword")
        anchor_element = etree.Element(
            "{http://www.isotc211.org/2005/gmx}Anchor",
            nsmap=nsmap
        )
        anchor_element.set("{http://www.w3.org/1999/xlink}href", f"https://deims.org/{site.get('PID', 'Error')}")
        anchor_element.text = site.get("name", "SitesNoName")
        keyword_element.append(anchor_element)

    add_language_code(data_identification, language_table.get(metadata.get('language')),
                      metadata.get('language'))

    extent = etree.SubElement(data_identification, "{http://www.isotc211.org/2005/gmd}extent")
    ex_extent = etree.SubElement(extent, "{http://www.isotc211.org/2005/gmd}EX_Extent")
    locations = metadata.get('geoLocations')
    for geolocation in locations:
        for locationKey, locationValue in geolocation.items():
            geographic_element = etree.SubElement(ex_extent, "{http://www.isotc211.org/2005/gmd}geographicElement")
            if locationKey == 'description':
                description = etree.SubElement(geographic_element,
                                               "{http://www.isotc211.org/2005/gmd}EX_GeographicDescription")
                geographic_identifier = etree.SubElement(description,
                                                         "{http://www.isotc211.org/2005/gmd}geographicIdentifier")
                md_identifier = etree.SubElement(geographic_identifier,
                                                 "{http://www.isotc211.org/2005/gmd}MD_Identifier")
                code = etree.SubElement(md_identifier, "{http://www.isotc211.org/2005/gmd}code")
                code.append(create_element("{http://www.isotc211.org/2005/gco}CharacterString", locationValue, nsmap))
            elif locationKey == 'EX_GeographicBoundingBox':
                bounding_box = etree.SubElement(geographic_element,
                                                "{http://www.isotc211.org/2005/gmd}EX_GeographicBoundingBox")
                west_bound_longitude = etree.SubElement(bounding_box,
                                                        "{http://www.isotc211.org/2005/gmd}westBoundLongitude")
                west_bound_longitude.append(
                    create_element("{http://www.isotc211.org/2005/gco}Decimal",
                                   str(locationValue['westBoundLongitude']),
                                   nsmap))
                east_bound_longitude = etree.SubElement(bounding_box,
                                                        "{http://www.isotc211.org/2005/gmd}eastBoundLongitude")
                east_bound_longitude.append(
                    create_element("{http://www.isotc211.org/2005/gco}Decimal",
                                   str(locationValue['eastBoundLongitude']),
                                   nsmap))
                south_bound_latitude = etree.SubElement(bounding_box,
                                                        "{http://www.isotc211.org/2005/gmd}southBoundLatitude")
                south_bound_latitude.append(
                    create_element("{http://www.isotc211.org/2005/gco}Decimal",
                                   str(locationValue['southBoundLatitude']),
                                   nsmap))
                north_bound_latitude = etree.SubElement(bounding_box,
                                                        "{http://www.isotc211.org/2005/gmd}northBoundLatitude")
                north_bound_latitude.append(
                    create_element("{http://www.isotc211.org/2005/gco}Decimal",
                                   str(locationValue['northBoundLatitude']),
                                   nsmap))


def add_geo_server_info(root, geo_server_info, nsmap):
    geo_service_type = geo_server_info.get('serviceType')
    geo_map_data = geo_server_info.get('mapData', [])
    if geo_server_info is None or geo_service_type is None or geo_map_data is None or geo_map_data == []:
        return

    distribution_info = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}distributionInfo")
    md_distribution = etree.SubElement(distribution_info, "{http://www.isotc211.org/2005/gmd}MD_Distribution")

    for map_data in geo_map_data:
        transfer_options = etree.SubElement(md_distribution, "{http://www.isotc211.org/2005/gmd}transferOptions")
        md_digital_transfer_options = etree.SubElement(transfer_options,
                                                       "{http://www.isotc211.org/2005/gmd}MD_DigitalTransferOptions")

        online = etree.SubElement(md_digital_transfer_options, "{http://www.isotc211.org/2005/gmd}onLine")
        ci_online_resource = etree.SubElement(online, "{http://www.isotc211.org/2005/gmd}CI_OnlineResource")

        linkage = etree.SubElement(ci_online_resource, "{http://www.isotc211.org/2005/gmd}linkage")
        linkage.append(
            create_element("{http://www.isotc211.org/2005/gco}CharacterString", map_data.get('path', 'Not defined'),
                           nsmap))

        name = etree.SubElement(ci_online_resource, "{http://www.isotc211.org/2005/gmd}name")
        name.append(
            create_element("{http://www.isotc211.org/2005/gco}CharacterString", map_data['features']['name'], nsmap))

        protocol = etree.SubElement(ci_online_resource, "{http://www.isotc211.org/2005/gmd}protocol")
        protocol.append(create_element("{http://www.isotc211.org/2005/gco}CharacterString", geo_service_type, nsmap))

        reference_system_info = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}referenceSystemInfo")
        md_reference_system = etree.SubElement(reference_system_info,
                                               "{http://www.isotc211.org/2005/gmd}MD_ReferenceSystem")
        reference_system_identifier = etree.SubElement(md_reference_system,
                                                       "{http://www.isotc211.org/2005/gmd}referenceSystemIdentifier")
        rs_identifier = etree.SubElement(reference_system_identifier, "{http://www.isotc211.org/2005/gmd}RS_Identifier")

        code = etree.SubElement(rs_identifier, "{http://www.isotc211.org/2005/gmd}code")
        epsg_code = str(map_data.get('epsgCode', 'epsg code not specified'))
        code.append(
            create_element("{http://www.isotc211.org/2005/gco}CharacterString", "EPSG:" + epsg_code, nsmap))

        code_space = etree.SubElement(rs_identifier, "{http://www.isotc211.org/2005/gmd}codeSpace")
        code_space.append(create_element("{http://www.isotc211.org/2005/gco}CharacterString", "EPSG", nsmap))

        md_spatial_representation_type = etree.SubElement(root,
                                                          "{http://www.isotc211.org/2005/gmd}spatialRepresentationType")
        map_data_type = map_data.get('type', 'Type not specified').lower()
        md_spatial_representation_type_code = etree.SubElement(md_spatial_representation_type,
                                                               "{http://www.isotc211.org/2005/gmd}MD_SpatialRepresentationTypeCode",
                                                               codeList="http://www.isotc211.org/2005/resources/codeList.xml#MD_SpatialRepresentationTypeCode",
                                                               codeListValue=map_data_type)
        md_spatial_representation_type_code.text = map_data_type


def generate_xml(json_data):
    metadata = json_data['metadata']
    nsmap = {
        "gmd": "http://www.isotc211.org/2005/gmd",
        "gco": "http://www.isotc211.org/2005/gco",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance",
        "xlink": "http://www.w3.org/1999/xlink",
        "gmx": "http://www.isotc211.org/2005/gmx",
        "gml": "http://www.opengis.net/gml"
    }

    root = create_root_element(nsmap)

    print(metadata)
    add_file_identifier(root, json_data.get('id'), nsmap)

    add_character_set(root)
    add_hierarchy_level(root)
    add_authors(root, metadata.get('authors', []), nsmap)
    add_date_stamp(root, get_current_datetime())
    add_identification_info(root, metadata, nsmap)
    add_license_info(root, metadata.get('licenses', []))
    add_temporal_extent_info(root, metadata.get('temporalCoverages', []))
    add_geo_server_info(root, metadata.get('geoServerInfo'), nsmap)

    tree = etree.ElementTree(root)
    xml_str = etree.tostring(tree, pretty_print=True, encoding=str)
    print(xml_str)
    return xml_str
    # print(xml_str.decode("UTF-8"))
