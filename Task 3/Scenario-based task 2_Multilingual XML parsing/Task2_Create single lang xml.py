import xml.etree.ElementTree as ET

# Define the path to your XML file
xml_file_path = 'C:\\Users\\sisil\\Documents\\1. Spring 2024\\Directed Study - LE\\3. File Format Walkthrough\\example2.xml'

# Function to keep only the selected language elements
def create_single_language_xml(root_element, language_code):
    # Create a deep copy of the tree so we can modify it without affecting the original
    new_tree = ET.ElementTree(ET.fromstring(ET.tostring(root_element, encoding='utf-8')))
    new_root = new_tree.getroot()
    
    # Iterate over all elements and remove non-target language child elements
    for parent in new_root.findall(".//"):
        # Make a list of child elements to remove
        children_to_remove = [child for child in parent if child.tag != language_code]
        
        # Remove the non-target language child elements
        for child in children_to_remove:
            parent.remove(child)
    
    return new_tree

# Language codes
languages = ['EN', 'ES', 'FR', 'AR']

# Parse the XML data from the file
tree = ET.parse(xml_file_path)
root = tree.getroot()

# Create and save a separate XML file for each language
for lang in languages:
    new_tree = create_single_language_xml(root, lang)
    new_tree.write(f'modified_{lang}.xml', encoding='utf-8', xml_declaration=True)