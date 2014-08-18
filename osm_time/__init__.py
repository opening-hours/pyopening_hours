# encoding: utf-8

__version__ = '0.1'

class ParseException(Exception):
    def __init__(self, value_to_parse, inner_message):
        self.message = u'Can‘t parse value: "{0}", {1}'.format(value_to_parse.replace('\n', ''), inner_message)
        Exception.__init__(self, self.message)

from .OpeningHours import *
