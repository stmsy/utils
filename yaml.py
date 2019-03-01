#!/usr/bin/env python

import yaml

YAML_EXTS = ['.yaml', '.yml']
LOAD_ERROR_MESSAGE = "file must be in YAML format"


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
