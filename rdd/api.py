# -*- coding: utf-8 -*-

"""
rdd.api
~~~~~~~

This module implements the Readability Shortener API.

"""

import requests

from .exceptions import *

__all__ = ['Readability']


class Readability(object):

    def __init__(self, url=None, verbose=None):
        self.url = url or 'http://www.readability.com/api/shortener/v1'
        self.verbose = verbose

    def _request(self, method, path, data=None, headers=None):
        url = self.url + path

        r = requests.request(method, url, data=data, headers=headers)
        r.raise_for_status()

        if self.verbose is not None:
            self.verbose.write(r.text + '\n')

        return r.json()

    def resources(self):
        """Retrieve information about sub-resources."""
        r = self._request('GET', '/')
        return r['resources']

    def shorten(self, full_url):
        """Create a new shortened URL."""
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = 'url=%s' % full_url
        r = self._request('POST', '/urls', data=data, headers=headers)
        if r.get('success') != True:
            raise ShortenerError('Failed to shorten %s' % full_url)
        return r['meta']

    def metadata(self, url_id):
        """Retrieve available metadata of a shortened link."""
        r = self._request('GET', '/urls/%s' % url_id)
        if r.get('success') != True:
            raise MetadataError('Failed to get metadata for %s' % url_id)
        return r['meta']
