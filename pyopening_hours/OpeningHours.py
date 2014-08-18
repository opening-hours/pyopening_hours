#!/usr/bin/env python
# encoding: utf-8
"""Quick and dirty abstraction layer for the JavaScript library
opening_hours.js. May use PyV8 or zerorpc in the future."""

import subprocess
import json
import os
import time
import socket
import tempfile

import dateutil.parser

class ParseException(Exception):
    def __init__(self, value_to_parse, inner_message):
        self.message = u'Can‘t parse value: "{0}", {1}'.format(value_to_parse.replace('\n', ''), inner_message)
        Exception.__init__(self, self.message)

class OpeningHours:
    _socket_path = os.path.join(tempfile.mkdtemp(), 'communicate.sock')

    __subprocess_param = [
        'node',
        '%s/node_modules/opening_hours/interactive_testing.js' %
        os.path.dirname(__file__),
        _socket_path]
    try:
        _oh_interpreter = subprocess.Popen(
            __subprocess_param,
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE
        )
    except OSError:
        __subprocess_param[0] = 'nodejs'
        _oh_interpreter = subprocess.Popen(
            __subprocess_param,
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE
        )
    time.sleep(0.1)
    __sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    __sock.connect(_socket_path)

    def __init__(self, value, nominatiomJSON=None, mode=None):
        """Constructs opening_hours object, given the opening_hours tag value."""
        # read description (meant for humans) from interactive_testing.js

        query = {'value': value.encode('UTF-8')}
        # print query
        try:
            self.__sock.send(query['value'])
        except IOError:
            # nodejs did notice that file "poh/osm_time/node_modules/opening_hours/interactive_testing.js" does not exist.
            # "Error: Cannot find module '$path_to_repo/osm_time/node_modules/opening_hours/interactive_testing.js'"
            raise ImportError(
                'Module was not installed properly. Please consult the README from pyopening_hours.')

        result_json = self.__sock.recv(23000)
        self._result_object = json.loads(result_json.decode('utf-8'))

        if self._result_object['error']:
            raise ParseException(value, self._result_object['eval_notes'])

    def getWarnings(self, *args):
        """Get parse warnings as list. Each warning is one string item in the
        list. Returns an empty list if there are no warnings."""
        return self._result_object['eval_notes']

    def prettifyValue(self, *args):
        """Get a nicely formated value."""
        return self._result_object['prettified']

    def getState(self, *args):
        """Check whether facility is `open' on the given date (or now)."""
        return self._result_object['state']

    def getUnknown(self, *args):
        """If the state of a amenity is conditional. Conditions can be
        expressed in comments.  True will only be returned if the state is
        false as the getState only returns true if the amenity is really open.
        So you may want to check the result of getUnknown if getState returned
        false."""
        return self._result_object['unknown']

    def getStateString(self, *args):
        """Return state string. Either 'open', 'unknown' or 'closed'."""
        return self._result_object['state_string']

    def getComment(self, *args):
        """Returns the comment."""
        try:
            return self._result_object['comment']
        except KeyError:
            return None

    def getNextChange(self, *args):
        """Returns time of next status change."""
        try:
            return dateutil.parser.parse(self._result_object['next_change'])
        except KeyError:
            return None

    def isWeekStable(self, *args):
        """Checks whether open intervals are same for every week."""
        return self._result_object['week_stable']

    def _neededNominatiomJson(self, *args):
        """Test if nominatiomJSON was *mandatory* to evaluate the value. For <variable_times> FIXME it is not mandatory."""
        return self._result_object['needed_nominatiom_json']

    def _getAll(self, *args):
        """Debugging: Get full result object as returned by interactive_testing.js"""
        return self._result_object
