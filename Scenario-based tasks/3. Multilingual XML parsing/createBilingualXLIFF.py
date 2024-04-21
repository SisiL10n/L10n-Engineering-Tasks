import xml.etree.ElementTree as ET

def find_text_in_element(element):
    if element is not None:
        for child in element:
            if child.text:
                return child.text
    return None

def create_xliff(source_file, target_file, target_language_code):
    # Parse the XML files for source and target languages
    source_tree = ET.parse(source_file)
    source_root = source_tree.getroot()

    target_tree = ET.parse(target_file)
    target_root = target_tree.getroot()

    # Create the root of the XLIFF file
    xliff = ET.Element('xliff', version='1.2', xmlns="urn:oasis:names:tc:xliff:document:1.2")
    file_element = ET.SubElement(xliff, 'file', {
        'source-language': 'EN',
        'target-language': target_language_code.upper(),
        'original': 'file.xml',
        'datatype': 'plaintext'
    })
    body = ET.SubElement(file_element, 'body')

    # Iterate over each element in the source file
    for source_question in source_root:
        for source_question_text in source_question:
            qid = source_question.tag
            source_lang_element = source_question_text.tag
            target_question = target_root.find(qid)

            # Create the <trans-unit> element for each question
            trans_unit = ET.SubElement(body, 'trans-unit', id=qid)

            # Add the source text
            source_text = ET.SubElement(trans_unit, 'source')
            source_text.text = source_question_text.text if source_question_text.text else ''

            # Add the target text
            target_text = ET.SubElement(trans_unit, 'target')
            if target_question is not None:
                target_lang_element = target_question.find(target_language_code.upper())
                target_text.text = target_lang_element.text if target_lang_element is not None and target_lang_element.text else ''
            else:
                target_text.text = ''

    # Generate the XLIFF file
    tree = ET.ElementTree(xliff)
    xliff_filename = f"Aligned_{target_language_code.lower()}.xliff"
    tree.write(xliff_filename, encoding='UTF-8', xml_declaration=True)
    print(f"Created XLIFF file: {xliff_filename}")

# Create the XLIFF file
create_xliff('modified_EN.xml', 'modified_ES.xml', 'es')
create_xliff('modified_EN.xml', 'modified_AR.xml', 'ar')
create_xliff('modified_EN.xml', 'modified_FR.xml', 'fr')