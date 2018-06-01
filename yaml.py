#!/usr/bin/env python

import yaml

from settings import LOAD_ERROR_MESSAGE


YAML_EXTS = ['yaml', 'yml']
YAML_LOAD_ERROR_MESSAGE = LOAD_ERROR_MESSAGE("YAML")


def load_yaml(filepath):
    """Load the YAML file and return as the Python dictionary."""
    with open(filepath, 'r') as f:
        return yaml.load(f)
