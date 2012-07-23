# -*- coding: utf-8 -*-

"""
rdd.exceptions
~~~~~~~~~~~~~~

This module contains the exceptions raised by rdd.

"""

from requests.exceptions import *


class ReadabilityException(RuntimeError):
    """Base class for Readability exceptions."""


class ShortenerError(ReadabilityException):
    """Failed to shorten URL."""


class MetadataError(ReadabilityException):
    """Failed to retrieve metadata."""
