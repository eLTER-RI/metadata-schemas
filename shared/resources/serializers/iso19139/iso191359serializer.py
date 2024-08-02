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
             "http://www.isotc211.org/2005/gmd http://schemas.opengis.net/iso/19139/20060504/gmd/gmd.xsd")
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
            create_element("{http://www.isotc211.org/2005/gco}CharacterString", author['fullName'], nsmap))

        contact_info = etree.SubElement(ci_responsible_party, "{http://www.isotc211.org/2005/gmd}contactInfo")
        ci_contact = etree.SubElement(contact_info, "{http://www.isotc211.org/2005/gmd}CI_Contact")
        address = etree.SubElement(ci_contact, "{http://www.isotc211.org/2005/gmd}address")
        ci_address = etree.SubElement(address, "{http://www.isotc211.org/2005/gmd}CI_Address")
        electronic_mail_address = etree.SubElement(ci_address,
                                                   "{http://www.isotc211.org/2005/gmd}electronicMailAddress")
        electronic_mail_address.append(
            create_element("{http://www.isotc211.org/2005/gco}CharacterString", author['email'], nsmap))

        role = etree.SubElement(ci_responsible_party, "{http://www.isotc211.org/2005/gmd}role")
        ci_role_code = etree.SubElement(role, "{http://www.isotc211.org/2005/gmd}CI_RoleCode",
                                        codeList="http://standards.iso.org/iso/19139/resources/gmxCodelists.xml#CI_RoleCode",
                                        codeListValue="pointOfContact")
        ci_role_code.text = "pointOfContact"


def add_identification_info(root, metadata, nsmap):
    identification_info = etree.SubElement(root, "{http://www.isotc211.org/2005/gmd}identificationInfo")
    data_identification = etree.SubElement(identification_info,
                                           "{http://www.isotc211.org/2005/gmd}MD_DataIdentification")

    citation = etree.SubElement(data_identification, "{http://www.isotc211.org/2005/gmd}citation")
    ci_citation = etree.SubElement(citation, "{http://www.isotc211.org/2005/gmd}CI_Citation")
    title = etree.SubElement(ci_citation, "{http://www.isotc211.org/2005/gmd}title")
    title.append(
        create_element("{http://www.isotc211.org/2005/gco}CharacterString", metadata['titles'][0]['text'], nsmap))

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
    for keyword in metadata['keywords']:
        keyword_element = etree.SubElement(md_keywords, "{http://www.isotc211.org/2005/gmd}keyword")
        keyword_element.append(create_element("{http://www.isotc211.org/2005/gco}CharacterString", keyword, nsmap))

    add_language_code(data_identification, language_table.get(metadata.get('language')),
                      metadata.get('language'))

    extent = etree.SubElement(data_identification, "{http://www.isotc211.org/2005/gmd}extent")
    ex_extent = etree.SubElement(extent, "{http://www.isotc211.org/2005/gmd}EX_Extent")
    for geolocation in metadata['geoLocations']:
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
            elif locationKey == 'box':
                bounding_box = etree.SubElement(geographic_element,
                                                "{http://www.isotc211.org/2005/gmd}EX_GeographicBoundingBox")
                west_bound_longitude = etree.SubElement(bounding_box,
                                                        "{http://www.isotc211.org/2005/gmd}westBoundLongitude")
                west_bound_longitude.append(
                    create_element("{http://www.isotc211.org/2005/gco}Decimal", str(locationValue['westLongitude']),
                                   nsmap))
                east_bound_longitude = etree.SubElement(bounding_box,
                                                        "{http://www.isotc211.org/2005/gmd}eastBoundLongitude")
                east_bound_longitude.append(
                    create_element("{http://www.isotc211.org/2005/gco}Decimal", str(locationValue['eastLongitude']),
                                   nsmap))
                south_bound_latitude = etree.SubElement(bounding_box,
                                                        "{http://www.isotc211.org/2005/gmd}southBoundLatitude")
                south_bound_latitude.append(
                    create_element("{http://www.isotc211.org/2005/gco}Decimal", str(locationValue['southLatitude']),
                                   nsmap))
                north_bound_latitude = etree.SubElement(bounding_box,
                                                        "{http://www.isotc211.org/2005/gmd}northBoundLatitude")
                north_bound_latitude.append(
                    create_element("{http://www.isotc211.org/2005/gco}Decimal", str(locationValue['northLatitude']),
                                   nsmap))


def generate_xml(json_data):
    metadata = json_data['metadata']
    nsmap = {
        "gmd": "http://www.isotc211.org/2005/gmd",
        "gco": "http://www.isotc211.org/2005/gco",
        "xsi": "http://www.w3.org/2001/XMLSchema-instance"
    }

    root = create_root_element(nsmap)

    print(metadata)
    add_file_identifier(root, json_data['id'], nsmap)

    add_character_set(root)
    add_hierarchy_level(root)
    add_authors(root, metadata['authors'], nsmap)
    add_date_stamp(root, get_current_datetime())
    add_identification_info(root, metadata, nsmap)

    tree = etree.ElementTree(root)
    xml_str = etree.tostring(tree, pretty_print=True, encoding=str)
    print(xml_str)
    return xml_str
    # print(xml_str.decode("UTF-8"))
