# pyopening_hours
Python module providing access to the [opening_hours.js][oh-lib] library which is written in JavaScript.

[oh-lib]: https://github.com/ypid/opening_hours.js

This python library only implements the [simple API](https://github.com/ypid/opening_hours.js#simple-api) from opening_hours.js at the moment (without optional parameters).

# Usage

```python
from osm_time.OpeningHours import OpeningHours, ParseException
import datetime

try:
    oh = OpeningHours('fail "not valid keyword"')
except ParseException as e:
    print e

value = 'Mon,Tu,Th,Fr 12:00-18:00; Samstag 12:00-17:00; Th[3] OFF; Th[-1] off'
oh = OpeningHours(value)
print 'Parsing complex value: %s' % value
print 'Is%s week stable' % ('' if oh.isWeekStable() else ' not')
print 'Facility is %s' % oh.getStateString()
print 'Next change in UTC: %s' % oh.getNextChange().strftime('%Y-%m-%d %H:%M:%S')
print 'Warnings:'
for line in oh.getWarnings():
    print '  %s' % line
```
