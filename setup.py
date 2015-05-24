#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2015, Peter Hillerström <peter.hillerstrom@gmail.com>
# All rights reserved. This software is licensed under the MIT license.
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.

from __future__ import with_statement

import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


PACKAGE_NAME = 'beautifulsoup4-slurp'
PACKAGE_VERSION = '0.0.2'
PACKAGES = ['slurp']


with open('README.rst', 'r') as readme:
    README_TEXT = readme.read()


setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    packages=PACKAGES,
    install_requires = [
        'argh >= 0.26.1',
        'beautifulsoup4 >= 4.3.2',
        'eight >= 0.3.2',
        'html5lib >= 0.99999',
        'lxml >= 3.4.4',
    ],
    scripts=['bin/slurp'],

    description="Slurp packages Beautifulsoup4 into command line.",
    long_description=README_TEXT,
    author='Peter Hillerström',
    author_email='peter.hillerstrom@gmail.com',
    license='MIT License',
    url='https://github.com/peterhil/slurp',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
        'Topic :: Utilities',
    ]
)
