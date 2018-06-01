#!/usr/bin/env python

import json

from settings import LOAD_ERROR_MESSAGE


JSON_EXTS = ['json', 'jsn']
JSON_LOAD_ERROR_MESSAGE = LOAD_ERROR_MESSAGE("JSON")


def load_json(filepath):
    """Load the JSON file and return as the Python dictionary."""
    with open(filepath, 'r') as f:
        return json.load(f)
