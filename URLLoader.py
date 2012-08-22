from __future__ import absolute_import

# python.
import urllib2 as _urllib2


class URLLoader(object):
    def __init__(self, baseURL):
        self._baseURL = baseURL

    def find_module(self, fullname, path):
        print 'find', fullname, path

    def load_module(self, *args):
        print 'load', len(args), args

