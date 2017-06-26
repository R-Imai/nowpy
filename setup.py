#! /usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import setuptools
    from setuptools import setup, find_packages
except ImportError:
    print("Please install setuptools.")

import info
import version


setup_opts = info.INFO
setup_opts["version"] = version.VERSION
setup_opts.update(dict(
    packages = find_packages("lib/nowpy"),
    package_dir = {"": "lib/nowpy"}
))

setup(**setup_opts)
