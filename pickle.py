#!/usr/bin/env python

import pickle

from settings import LOAD_ERROR_MESSAGE


PICKLE_EXTS = ['pickle', 'pckl', 'pkl', 'dump']
PICKLE_LOAD_ERROR_MESSAGE = LOAD_ERROR_MESSAGE("PICKLE")
KEYERROR_MESSAGE = "key must coincide with the filename w/o extension"


def create_key(filepath):
    """Create the dictionary key from the given filepath."""
    return filepath.split('/')[-1].split('.')[0]


def load_dumped_data(filepath):
    """Load the PICKLE file and return as the Python object."""
    key = create_key(filepath)
    with open(filepath, 'rb') as f:
        try:
            data = pickle.load(f)[key]
        except KeyError:
            raise KeyError(KEYERROR_MESSAGE)
    return data


def pickle_data(filepath, data_dict):
    """Dump the data to the specified location."""
    key = create_key(filepath)
    key_list = list(data_dict.keys())
    if key == key_list[0]:
        with open(filepath, 'wb') as f:
            pickle.dump(data_dict, f)
    else:
        raise KeyError(KEYERROR_MESSAGE)
