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


def die(msg):
    sys.exit('error: %s' % msg)


def main():
    parser = optparse.OptionParser()
    parser.add_option('-u', '--url',
                      action='store',
                      default=os.environ.get('RDD_URL'))
    parser.add_option('-v', '--verbose',
                      action='store_true',
                      default=os.environ.get('RDD_VERBOSE'))
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
    import json
    print json.dumps(data, indent=4)
