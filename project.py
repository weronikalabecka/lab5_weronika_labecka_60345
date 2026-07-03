import sys
import json
import yaml
import xml.etree.ElementTree as ET
import os

def get_extension(path):
    return os.path.splitext(path)[1].lower()
