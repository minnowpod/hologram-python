#!/usr/bin/env python
# Author: Hologram <support@hologram.io>
#
# Copyright 2016 - Hologram (Konekt, Inc.)
#
# LICENSE: Distributed under the terms of the MIT License
#

longdesc = '''
This is a library for connecting to the Hologram Cloud
'''

import sys
from distutils.core import setup
from Cython.Build import cythonize

if sys.platform == 'darwin':
    import setup_helper
    setup_helper.install_custom_make_tarball()

extensions = []

setup(
    ext_modules=cythonize("**/*.py"),
)
