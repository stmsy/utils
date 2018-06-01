#!/usr/bin/env python

import os


def make_dir(dirpath, mode=0o755):
    """Make a single directory with the specified permission. Ignore 
    FileExistsError when the error raised.

    Argument:
      dirpath (str): the absolute path of the directory to be created
    """
    try:
        os.mkdir(dirpath, mode=mode)
    except FileExistsError:
        pass


def is_with_ext(filename):
    """Check whether the filename contains the file extension."""
    if '.' in filename:
        return True
    else
        return False


def is_filename_valid(filename, exts):
    """Check whether the filename is valid."""
    if filename.split('.')[1] in exts:
        return True
    else:
        return False


def get_filename(filepath):
    """Get the filename from the specified absolute/relative filepath."""
    return filepath.split('/')[-1]


def get_filenames(dirpath, exts):
    """Return a list of the filenames with the specified extention."""
    filenames = os.listdir(dirpath)
    filenames = [
        filename for filename in filenames if is_filename_valid(filename, exts)
    ]
    return filenames
