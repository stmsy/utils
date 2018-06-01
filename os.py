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
