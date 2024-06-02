from lxml import etree
import datetime

# Function to get the file path of the TMX file and the output file path
def get_file_paths():
    tmx_file_path = input("Enter the path of the TMX file: ")
    output_file_path = input("Enter the path for the output file: ")
    return tmx_file_path, output_file_path

# Function to deduplicate the TMX file based on the x-ID values
def deduplicate_tmx(tmx_file_path, output_file_path):
    # Open the tmx file
    parser = etree.XMLParser(ns_clean=True)
    tree = etree.parse(tmx_file_path, parser)
    root = tree.getroot()

    # count the number of translation units in the file
    initial_count = len(root.findall('.//tu'))
    print("Initial unit count: ", initial_count)

    # Dictionary to count occurrences of each x-ID
    x_id_count = {}
    # List to store old translation units
    backup_list = []

    # Loop through all translation units to count the occurance of each x-ID
    for tu in root.findall(".//tu"):
        x_id_elements = tu.xpath(".//prop[@type='x-ID']/text()")
        if x_id_elements:
            x_id = x_id_elements[0]
            if x_id in x_id_count:
                x_id_count[x_id] += 1
            else:
                x_id_count[x_id] = 1

    # List to store all duplicated x-id values
    duplicated_x_id_list = [x_id for x_id, count in x_id_count.items() if count > 1]

    # Count the number of duplicated x-id values
    duplicated_count = len(duplicated_x_id_list)
    print("duplicated unit count: ", duplicated_count)

    # Loop through all translation units to extract the duplicated x-id values
    for stringId in duplicated_x_id_list:
        print(f"Extracting entries with duplicate xid {stringId}...")
        
        # XPath to select translation units with duplicate xids as the value of the prop element
        xPathSelect = f"//tu[prop[@type='x-ID' and text()='{stringId}']]"
        
        # Select all TU entries with duplicate xid
        elementsDup = root.xpath(xPathSelect)
        
        print(f"There are {len(elementsDup)} elements in this duplicate container with xid {stringId}")
        
        # Sort the entries based on the change date
        elementsDup.sort(key=lambda e: datetime.datetime.strptime(e.get('changedate'), "%Y%m%dT%H%M%SZ"))
        
        # If there are more than 2 entries with duplicate xid, remove until there are only two of them
        if len(elementsDup) > 2:
            print(f"For xid {stringId}, more than 2 entries are found. Process initiated to remove until there are only two.")
            while len(elementsDup) > 2:
                elementToBeRemoved = elementsDup.pop(0)  # Remove the oldest
                elementToBeRemoved.getparent().remove(elementToBeRemoved)
                backup_list.append(elementToBeRemoved)

    # Create backup list
    backup_root = etree.Element("tmx", version="1.4")
    backup_body = etree.SubElement(backup_root, "body")
    for element in backup_list:
        backup_body.append(element)

    # Write the backup list to a TMX file
    backup_tree = etree.ElementTree(backup_root)
    backup_tree.write(output_file_path + 'backup.tmx', pretty_print=True, xml_declaration=True, encoding='UTF-8')

    # Write the modified original XML tree to a new TMX file
    original_tree = etree.ElementTree(root)
    original_tree.write(output_file_path + 'updated.tmx', pretty_print=True, xml_declaration=True, encoding='UTF-8')

    print("Backup and updated TMX files have been generated.")

# Call the get_file_paths and deduplicate_tmx functions
tmx_file_path, output_file_path = get_file_paths()
deduplicate_tmx(tmx_file_path, output_file_path)