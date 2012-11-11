# -*- coding: utf-8 -*-

import os
import sys

rdd_root = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', '..')
sys.path.insert(0, rdd_root)

import pytest
from httpretty import HTTPretty, httprettified
from rdd import Readability


def fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)

def fixture(filename):
    return open(fixture_path(filename)).read()

def rdd_url(path):
    return 'http://www.readability.com/api/shortener/v1' + path


class TestReadability(object):

    def setup_class(self):
        HTTPretty.enable()
        self.readability = Readability()

    def teardown_class(self):
        HTTPretty.disable()

    def test_resources(self):
        HTTPretty.register_uri(HTTPretty.GET, rdd_url('/'),
                               body=fixture('resources.json'))
        resources = self.readability.resources()
        assert resources['urls/:id']['href'] == '/api/shortener/v1/urls/:id'
        assert resources['urls']['href'] == '/api/shortener/v1/urls'

    def test_shorten(self):
        full_url = 'http://www.paulgraham.com/gh.html'
        url_id = 'ga4qf47t'
        HTTPretty.register_uri(HTTPretty.POST, rdd_url('/urls'),
                               body=fixture('shorten.json'))
        meta = self.readability.shorten(full_url)
        assert meta['url'] == '/api/shortener/v1/urls/%s' % url_id
        assert meta['rdd_url'] == 'http://rdd.me/%s' % url_id
        assert meta['id'] == url_id

    def test_metadata(self):
        url_id = 'ga4qf47t'
        HTTPretty.register_uri(HTTPretty.GET, rdd_url('/urls/%s' % url_id),
                               body=fixture('metadata.json'))
        meta = self.readability.metadata(url_id)
        assert meta['article']['url'] == 'http://www.paulgraham.com/gh.html'
        assert meta['article']['title'] == 'Great Hackers'
        assert meta['article']['excerpt'].startswith('Want to start a startup?')
        assert meta['article']['word_count'] == 5147
        assert meta['article']['author'] is None
        assert meta['rdd_url'] == 'http://rdd.me/%s' % url_id
        assert meta['id'] == url_id
        assert meta['full_url'] == 'http://readability.com/articles/%s' % url_id


if __name__ == '__main__':
    pytest.main(__file__)
