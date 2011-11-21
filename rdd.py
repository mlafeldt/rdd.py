#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Readability API implementation

The API is described at https://www.readability.com/publishers/rdd
"""

import requests
import simplejson as json


class Request(object):

    _JSON_MEDIA_TYPE = 'application/json'

    def __init__(self, url=None, verbose=None):
        self.url = url or 'https://readability.com/api/shortener/v1'
        self.config = {}
        if verbose is not None:
            self.config = {'verbose': verbose}

    def _request(self, method, path, data=None):
        headers = None
        if data is not None:
            # XXX Dunno why the API isn't using JSON for requests too?
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}

        url = self.url + path
        r = requests.request(method, url, data=data, headers=headers,
                             config=self.config)
        r.raise_for_status()

        if not self._JSON_MEDIA_TYPE in r.headers['Content-Type']:
            raise TypeError('No JSON in response')

        return json.loads(r.content) if r.content.strip() else None

    def get(self, *args, **kwargs):
        return self._request('GET', *args, **kwargs)

    def post(self, *args, **kwargs):
        return self._request('POST', *args, **kwargs)


class Readability(object):

    def __init__(self, request):
        self.request = request

    def resources(self):
        """Retrieve information about sub-resources."""
        return self.request.get('/')

    def shorten(self, full_url):
        """Create a new shortened URL."""
        return self.request.post('/urls', data='url=%s' % full_url)

    def metadata(self, url_id):
        """Retrieve available metadata of a shortened link."""
        return self.request.get('/urls/%s' % url_id)


if __name__ == '__main__':
    import sys

    request = Request(verbose=sys.stderr)
    readability = Readability(request)

    if (sys.argv[1] == 'resources'):
        data = readability.resources()
    elif (sys.argv[1] == 'shorten'):
        data = readability.shorten(sys.argv[2])
    elif (sys.argv[1] == 'metadata'):
        data = readability.metadata(sys.argv[2])

    # HACK re-encode json for pretty output
    print json.dumps(data, indent=4)
