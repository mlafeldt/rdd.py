# -*- coding: utf-8 -*-

"""
rdd.cli
~~~~~~~

This module implements the command-line interface to the Readability
Shortener API.

"""

import sys
import os
import optparse

from .api import Readability
from .exceptions import RequestException, ReadabilityException

__all__ = ['main']


def die(msg):
    sys.exit('error: %s' % msg)


def pp(d, indent=0):
    for k, v in list(sorted(d.items())):
        print('  ' * indent + str(k) + ':')
        if isinstance(v, dict):
            pp(v, indent + 1)
        else:
            print('  ' * (indent + 1) + str(v))


def main(argv=None):
    parser = optparse.OptionParser()
    parser.add_option('-u', '--url',
                      help='set URL of Readability shortener service',
                      action='store',
                      default=os.environ.get('RDD_URL'))
    parser.add_option('-v', '--verbose',
                      help='be a bit more verbose',
                      action='store_true',
                      default=os.environ.get('RDD_VERBOSE'))
    opts, args = parser.parse_args(argv)

    if len(args) < 1:
        die('command missing')

    verbose = sys.stderr if opts.verbose else None
    readability = Readability(url=opts.url, verbose=verbose)

    try:
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
    except (RequestException, ReadabilityException) as e:
        die('%s: %s' % (e.__class__.__name__, e))

    pp(data)
