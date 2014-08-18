#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup

setup(
    name         = 'pyopening_hours',
    version      = '0.1',
    description  = 'Python module providing access to the opening_hours.js library which is written in JavaScript.',
    author       = 'Robin `ypid` Schneider',
    author_email = 'ypid23@aol.de',
    url          = 'https://github.com/ypid/pyopening_hours',
    packages     = ['pyopening_hours'],
    license      = 'GPLv3',
    test_suite   = 'tests',
    keywords     = ['OSM', 'OpenStreetMap', 'opening_hours'],
    install_requires=[
        'unittest2',
        'python-dateutil',
    ],
)
