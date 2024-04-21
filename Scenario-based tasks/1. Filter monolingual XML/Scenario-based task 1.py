import xml.etree.ElementTree as ET

# Parse the XML file
tree = ET.parse('example.xml')
root = tree.getroot()

# Function to check if a string is 'num' followed by an even number
def check_name_attr(string_element):
    # Get the 'name' attribute of the string element
    name = string_element.get('name')
    # Check if the 'name' starts with 'num'
    if name and name.startswith('num'):        
        # Extract the part of the 'name' after 'num'
        num_part = name[3:]        
        # Check if the extracted part is a digit and an even number
        if num_part.isdigit() and int(num_part) % 2 == 0:
            return True
    return False

# Search for all elements where the 'name' attribute is 'num' followed by an even number
for string in root.iter('string'):
    if check_name_attr(string):
        string.set('class', 'need')  # Add a 'class' attribute with value 'need'

# Print the modified XML
print(ET.tostring(root, encoding='unicode'))

# Save the modified XML to a file
tree.write('modifiedexample.xml', encoding='utf-8', xml_declaration=True)