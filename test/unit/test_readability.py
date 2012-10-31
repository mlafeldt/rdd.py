# -*- coding: utf-8 -*-

import pytest
import mock
import rdd


class TestReadability(object):

    def setup_method(self, method):
        self.readability = rdd.Readability()
        self.request = mock.Mock()
        self.readability._request = self.request

    def test_resources(self):
        resources = {} # TODO
        self.request.return_value = {'resources': resources}
        assert self.readability.resources() == resources
        self.request.assert_called_once_with('GET', '/')

    def test_shorten(self):
        meta = {} # TODO
        self.request.return_value = {'meta': meta, 'messages': [], 'success': True}
        assert self.readability.shorten('some_url') == meta
        self.request.assert_called_once_with('POST', '/urls',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data='url=some_url')

    def test_metadata(self):
        meta = {} # TODO
        self.request.return_value = {'meta': meta, 'messages': [], 'success': True}
        assert self.readability.metadata('some_id') == meta
        self.request.assert_called_once_with('GET', '/urls/some_id')


if __name__ == '__main__':
    pytest.main(__file__)
