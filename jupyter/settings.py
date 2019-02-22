#!/usr/bin/env python

from pathlib import Path

CWD = Path.cwd()
# Project root dir will be named notebooks
PROJECT_ROOT = CWD.joinpath('..', '..').resolve()  
DATA_DIR = PROJECT_ROOT.joinpath('data')
