#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='almond',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Edit JSON as YAML",
    long_description="Edit JSON as YAML in Vim.",
    scripts=['almond'],
    data_files=[('share/man/man1', ['almond.1'])],
)
