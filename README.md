# pyopening_hours

[![Build Status](https://travis-ci.org/ypid/pyopening_hours.svg?branch=master)](https://travis-ci.org/ypid/pyopening_hours)

Python module providing access to the [opening_hours.js][oh-lib] library which is written in JavaScript.

This python library only implements the [simple API](https://github.com/opening-hours/opening_hours.js#simple-api) from opening_hours.js at the moment (without optional parameters).

## Installation

Install [pyopening_hours](https://pypi.python.org/pypi/pyopening_hours/) simply by using pip:

```Shell
pip install pyopening_hours
```

## Usage

```python
import pyopening_hours

try:
    oh = pyopening_hours.OpeningHours('Lun-')
except pyopening_hours.ParseException as error:
    print(error.message)

value = 'Mon,Tu,Th,Fr 12:00-18:00; Samstag 12:00-17:00 "I ❤ unicode"; Th[3] OFF; Th[-1] off'
oh = pyopening_hours.OpeningHours(value)
print(f"Parsing complex value: {value}")
print(f"Is{'' if oh.isWeekStable() else ' not'} week stable")
print(f"Facility is {oh.getStateString()}")
print(f"Next change in UTC: {oh.getNextChange().strftime('%Y-%m-%d %H:%M:%S')}")
print("Warnings:")
for line in oh.getWarnings():
    print('  ' + line)
```

## Development

Just clone the repository with

```Shell
git clone https://github.com/opening-hours/pyopening_hours
```

and install it’s dependencies (execute inside the repository):
```Shell
make dependencies-get
```

## Used by other projects

This library is used in the following projects:

* [opening_hours_bot][]

## Other modules

* [osm-opening-hours](https://github.com/martinfilliau/osm-opening-hours) (pure python implementation)
* [Python_OpeningHours](https://github.com/anthill/Python_OpeningHours)


[oh-lib]: https://github.com/opening-hours/opening_hours.js
[opening_hours_bot]: https://github.com/ypid/opening_hours_bot
