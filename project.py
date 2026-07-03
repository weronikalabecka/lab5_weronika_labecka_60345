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
