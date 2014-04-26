#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup

setup(name         = 'pyopening_hours',
      version      = '0.1',
      description  = 'Python module providing access to the opening_hours.js library which is written in JavaScript.',
      author       = 'Robin `ypid` Schneider',
      author_email = 'ypid23@aol.de',
      url          = 'https://github.com/ypid/pyopening_hours',
      packages     = ['osm_time'],
      package_dir  = {'osm_time': 'osm_time/'},
      package_data = {'osm_time': [' node_modules/*']}, # WTF, the first character in this list is ignored?
      license      = 'BSD',
      test_suite   = 'tests',
     )
