#!/usr/bin/env python

from pathlib import Path

CWD = Path.cwd()
# Project root dir will be named notebooks
PROJECT_ROOT = CWD.joinpath('..').resolve()  
DATA_DIR = PROJECT_ROOT.joinpath('data')


def get_line(num_width, line_type='-'):
    """Define a horisontal line to fulfill the cell."""
    return line_type * num_width
