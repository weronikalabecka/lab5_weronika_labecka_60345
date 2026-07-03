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
    