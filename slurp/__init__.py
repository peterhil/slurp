#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2015, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under the MIT license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from __future__ import (print_function, division, unicode_literals, absolute_import)

import argh
import argparse
import codecs
import eight
import subprocess
import sys

from bs4 import BeautifulSoup
from eight import *


eight.wrap_stdio()
eight.decode_command_line_args()


def character_encoding(file_path):
    if sys.version_info < (2, 7, 0):
        import commands
        return commands.getoutput('file -b --mime-encoding %s' % file_path)
    return bytes.decode(subprocess.check_output(['file', '-b', '--mime-encoding', file_path]))


def error_exit(err):
    sys.stderr.write("{}: {}\n".format(err.__class__.__name__, err))
    return sys.exit(err.errno)


def read(infile):
    try:
        if infile == '-':
            return sys.stdin.read()
        else:
            with codecs.open(infile, 'rb', character_encoding(infile)) as f:
                inf = codecs.getwriter('utf-8')(f)
                return inf.read()
    except IOError as err:
        return error_exit(err)


def write(output, data):
    try:
        if output == '-':
            return print(data)
        else:
            with codecs.open(output, 'wb', 'utf-8-sig') as f:
                return f.write(data + "\n")
    except IOError as err:
        return error_exit(err)

        
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
    return write(output, html)


def main():
    parser = argparse.ArgumentParser()
    argh.set_default_command(parser, slurp)
    argh.dispatch(parser)


if __name__ == '__main__':
    main()
