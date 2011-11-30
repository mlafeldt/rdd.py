# -*- coding: utf-8 -*-

"""Python implementation of the Readability Shortener API"""

import requests
try:
    import simplejson as json
except ImportError:
    import json


class Readability(object):

    def __init__(self, url=None, verbose=None):
        self.url = url or 'https://readability.com/api/shortener/v1'
        self.verbose = verbose

    def _request(self, method, path, data=None, headers=None):
        url = self.url + path

        config = {}
        if self.verbose is not None:
            config['verbose'] = self.verbose

        r = requests.request(method, url, data=data, headers=headers,
                             config=config, allow_redirects=True)
        r.raise_for_status()

        if not 'application/json' in r.headers['Content-Type']:
            raise TypeError('No JSON in response')

        content = r.content.strip()
        if content:
            if self.verbose is not None:
                self.verbose.write(content + '\n')
            return json.loads(content)
        else:
            return None

    def resources(self):
        """Retrieve information about sub-resources."""
        return self._request('GET', '/')

    def shorten(self, full_url):
        """Create a new shortened URL."""
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = 'url=%s' % full_url
        return self._request('POST', '/urls', data=data, headers=headers)

    def metadata(self, url_id):
        """Retrieve available metadata of a shortened link."""
        return self._request('GET', '/urls/%s' % url_id)
