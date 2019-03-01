#!/usr/bin/env python

import yaml

from settings import LOAD_ERROR_MESSAGE


YAML_EXTS = ['.yaml', '.yml']
YAML_LOAD_ERROR_MESSAGE = LOAD_ERROR_MESSAGE("YAML")


def load_yaml(filepath):
    """Load the YAML file and return as the Python dictionary."""
    if filepath.suffix in YAML_EXTS:
        try:
            with filepath.open('r') as f:
                return yaml.load(f)
        except:
            raise Exception("YAML file load failed")
    else:
        raise Exception(YAML_LOAD_ERROR_MESSAGE)
