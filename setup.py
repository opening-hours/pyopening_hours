#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup
import os
import codecs

long_description = ''
if os.path.exists('README.rst'):
    long_description = codecs.open('README.rst', encoding='UTF-8', mode='r').read(),

setup(
    name         = 'pyopening_hours',
    version      = '0.3.0',
    description  = 'Python module providing access to the opening_hours.js library which is written in JavaScript.',
    author       = 'Robin `ypid` Schneider',
    author_email = 'ypid23@aol.de',
    url          = 'https://github.com/ypid/pyopening_hours',
    packages     = ['pyopening_hours'],
    license      = 'GPLv3',
    test_suite   = 'tests',
    keywords     = ['OSM', 'OpenStreetMap', 'opening_hours'],
    package_data = {
        'pyopening_hours': [
            'node_modules/opening_hours/node_modules/suncalc/suncalc.js',
            'node_modules/opening_hours/node_modules/suncalc/package.json',
            'node_modules/opening_hours/opening_hours.js',
            'node_modules/opening_hours/package.json',
            'node_modules/opening_hours/interactive_testing.js',
        ]
    },
    install_requires=[
        'unittest2',
        'python-dateutil',
    ],
    long_description = long_description,
)
