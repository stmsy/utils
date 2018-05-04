#!/usr/bin/env python
# -*- coding: utf-8 -*-

# The config script is necessary for Python 2.7.

try:
    import apport_python_hook
except ImportError:
    pass
else:
    apport_python_hook.install()
import sys
sys.setdefaultencoding('utf-8')
