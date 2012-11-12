# -*- coding: utf-8 -*-

import json
import mock
import os
import sys

rdd_root = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..')
sys.path.insert(0, rdd_root)

import pytest
import rdd


def load_fixture(filename):
    path = os.path.join(os.path.dirname(__file__), 'fixtures', filename)
    return json.load(open(path))


class TestReadability(object):

    def setup_method(self, method):
        self.readability = rdd.Readability()
        self.request = mock.Mock()
        self.readability._request = self.request

    def test_resources(self):
        json = load_fixture('resources.json')
        self.request.return_value = json
        assert self.readability.resources() == json['resources']
        self.request.assert_called_once_with('GET', '/')

    def test_shorten(self):
        full_url = 'http://www.paulgraham.com/gh.html'
        json = load_fixture('shorten.json')
        self.request.return_value = json
        assert self.readability.shorten(full_url) == json['meta']
        self.request.assert_called_once_with('POST', '/urls', data='url=%s' % full_url,
            headers={'Content-Type': 'application/x-www-form-urlencoded'})

    def test_metadata(self):
        url_id = 'ga4qf47t'
        json = load_fixture('metadata.json')
        self.request.return_value = json
        assert self.readability.metadata(url_id) == json['meta']
        self.request.assert_called_once_with('GET', '/urls/%s' % url_id)


if __name__ == '__main__':
    pytest.main(__file__)
