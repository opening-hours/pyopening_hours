# pyopening_hours
Python module providing access to the [opening_hours.js][oh-lib] library which is written in JavaScript.

[oh-lib]: https://github.com/ypid/opening_hours.js

This python library only implements the [simple API](https://github.com/ypid/opening_hours.js#simple-api) from opening_hours.js at the moment (without optional parameters).

## Install

Just clone the repository with

```
git clone https://github.com/ypid/pyopening_hours
```

and install it’s dependencies (execute inside the repository):
```
npm install
```

## Usage

```python
from osm_time.OpeningHours import OpeningHours, ParseException
import datetime

try:
    oh = OpeningHours(u'Lun-') # Returns except message with unicode ;)
except ParseException as e:
    print unicode(e.message).encode("utf-8")

value = u'Mon,Tu,Th,Fr 12:00-18:00; Samstag 12:00-17:00 "I ❤ unicode"; Th[3] OFF; Th[-1] off'
oh = OpeningHours(value)
print 'Parsing complex value: %s' % value
print 'Is%s week stable' % ('' if oh.isWeekStable() else ' not')
print 'Facility is %s' % oh.getStateString()
print 'Next change in UTC: %s' % oh.getNextChange().strftime('%Y-%m-%d %H:%M:%S')
print 'Warnings:'
for line in oh.getWarnings():
    print '  %s' % line
```

## Used by other projects
This library is used in the following projects:

* [opening\_hours\_bot][]

[opening\_hours\_bot]: https://github.com/ypid/opening_hours_bot

## Other modules
* [osm-opening-hours](https://github.com/martinfilliau/osm-opening-hours) (pure python implementation)
