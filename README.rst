Slurp the beautiful soup
===============

BeautifulSoup4 packaged into a command line tool.


Installation
---------

From the Python package index (Pypi_):

    (sudo) pip install beautifulsoup4-slurp

or from Github_:

    git clone https://github.com/peterhil/slurp.git
    cd slurp
    (sudo) python setyp.py install


Usage
-----

Show help:

    slurp -h

Parse with html5lib and pretty print into stdout:

    slurp -i bookmarks.html -p 'html5lib' -y

Parse with lxml and pretty print into stdout:

    slurp -i bookmarks.html -p 'lxml' -y

Write pretty-printed to output to file:

    slurp -y -i bookmarks.html -o bookmarks_soup.html

Pipe into slurp:

    echo '<title>Slurp!</title><p><a href="https://github.com/peterhil/slurp/">Github</a>' | slurp -y


 .. _Github: https://github.com/peterhil/slurp/
.. _Pypi: http://pypi.python.org/pypi/beautifulsoup4-slurp


License
------

Copyright (c) 2015, Peter Hillerström <peter.hillerstrom@gmail.com>  
All rights reserved. This software is licensed under MIT license.

For the full copyright and license information, please view the LICENSE  
file that was distributed with this source code.
