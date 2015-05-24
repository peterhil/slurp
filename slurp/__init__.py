#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2015, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under the MIT license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from __future__ import print_function

import argh
import argparse
import codecs
import commands
import sys

from bs4 import BeautifulSoup


def character_encoding(file_path):
    return commands.getoutput('file -b --mime-encoding %s' % file_path)


def error_exit(err):
    sys.stderr.write("{}: {}\n".format(err.__class__.__name__, err))
    return sys.exit(err.errno)


def read(input):
    try:
        if input == '-':
            return sys.stdin.read()
        else:
            with codecs.open(input, 'rb', character_encoding(input)) as f:
                return f.read()
    except IOError, e:
        return error_exit(e)


def write(output, data):
    try:
        if output == '-':
            return sys.stdout.write(data)
        else:
            with codecs.open(output, 'wb', 'utf-8-sig') as f:
                return f.write(data)
    except IOError, e:
        return error_exit(e)

        
class recursion_limit:
    def __init__(self, limit):
        self.limit = limit
    def __enter__(self):
        self.orig_limit = sys.getrecursionlimit()
        sys.setrecursionlimit(self.limit)
        return
    def __exit__(self, type, value, traceback):
        sys.setrecursionlimit(self.orig_limit)


def parse(doc, parser, max_rec):
    with recursion_limit(max_rec):
        html = BeautifulSoup(doc, parser)
    return html


@argh.arg('-y', '--pretty', default=False, help='pretty print the HTML output')
def slurp(input='-', output='-', parser='html5lib', recursion=2000, **options):
    doc = read(input)
    html = parse(doc, parser, recursion)
    if options['pretty']:
        html = html.prettify()
    return write(output, unicode(html) + "\n")


def main():
    parser = argparse.ArgumentParser()
    argh.set_default_command(parser, slurp)
    argh.dispatch(parser)


if __name__ == '__main__':
    main()
