#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Readability API implementation

The API is described at https://www.readability.com/publishers/rdd
"""

import requests
try:
    import simplejson as json
except ImportError:
    import json


class Readability(object):

    def __init__(self, url=None, verbose=None):
        self.url = url or 'https://readability.com/api/shortener/v1'
        self.config = {}
        if verbose is not None:
            self.config['verbose'] = verbose

    def _request(self, method, path, data=None, headers=None):
        url = self.url + path
        r = requests.request(method, url, data=data, headers=headers,
                             config=self.config, allow_redirects=True)
        r.raise_for_status()

        if not 'application/json' in r.headers['Content-Type']:
            raise TypeError('No JSON in response')

        return json.loads(r.content) if r.content.strip() else None

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


if __name__ == '__main__':
    import sys
    import optparse

    def die(msg):
        sys.exit('error: %s' % msg)

    parser = optparse.OptionParser()
    parser.add_option('-u', '--url', action='store')
    parser.add_option('-v', '--verbose', action='store_true')
    opts, args = parser.parse_args()

    if len(args) < 1:
        die('command missing')

    verbose = sys.stderr if opts.verbose else None
    readability = Readability(url=opts.url, verbose=verbose)

    cmd = args[0]
    if cmd in ('resources', 'r'):
        data = readability.resources()
    elif cmd in ('shorten', 's'):
        if len(args) < 2:
            die('argument missing')
        data = readability.shorten(args[1])
    elif cmd in ('metadata', 'm'):
        if len(args) < 2:
            die('argument missing')
        data = readability.metadata(args[1])
    else:
        die('invalid command')

    # HACK re-encode json for pretty output
    print json.dumps(data, indent=4)
