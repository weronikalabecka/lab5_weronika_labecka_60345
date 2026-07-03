import sys
import json
import yaml
import xml.etree.ElementTree as ET
import os

def get_extension(path):
    return os.path.splitext(path)[1].lower()

def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
def write_json(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

def read_yaml(path):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)
    
def write_yaml(data, path):
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f)

def xml_to_dict(element):
    result = {}
    for child in element:
        if list(child):
            result[child.tag]=xml_to_dict(child)
        else:
            result[child.tag]=child.text
    return result

def dict_to_xml(data, root_name="root"):
    root = ET.Element(root_name)

    def build(elem, data):
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.SubElement(elem, key)
                build(child, value)
            else:
                elem.text = str(data)
    build(root, data)
    return root

def read_xml(path):
    tree = ET.parse(path)
    return xml_to_dict(tree.getroot())

def write_xml(data, path):
    root = dict_to_xml(data)
    tree = ET.ElementTree(root)
    tree.write(path, encoding='utf-8', xml_declaration=True)
    
def main():
    if len(sys.argv) != 3:
        print("Wzór: python3 project.py input.xxx output.xxx")
        return
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    in_ext = get_extension(input_file)
    out_ext = get_extension(output_file)

    if in_ext == ".json":
        data = read_json(input_file)
    elif in_ext in [".yml", ".yaml"]:
        data = read_yaml(input_file)
    elif in_ext == ".xml":
        data = read_xml(input_file)
    else:
        print("Nieznany format")
        return
    
    if out_ext == ".json":
        write_json(data, output_file)
    elif out_ext in [".yml", ".yaml"]:
        write_yaml(data, output_file)
    elif out_ext == ".xml":
        write_xml(data, output_file)
    else:
        print("Nieznany format")
        return
    
    print("koniec")

if __name__ == "__main__":
    main()