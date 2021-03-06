BeautifulSoup4_ packaged into a command line tool.
=================================================

For now this tool just parses `HTML tag soup`_ with BeautifulSoup4,
and writes out the results. This can help for example to properly parse
the structure of a Netscape bookmarks file, which omits many ending tags.


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
.. _Beautifulsoup4: http://www.crummy.com/software/BeautifulSoup/
.. _`HTML tag soup`: https://en.wikipedia.org/wiki/Tag_soup


License
------

Copyright (c) 2015, Peter Hillerström <peter.hillerstrom@gmail.com>  
All rights reserved. This software is licensed under MIT license.

For the full copyright and license information, please view the LICENSE  
file that was distributed with this source code.

.. image:: https://img.shields.io/pypi/v/beautifulsoup4-slurp.svg
        :target: https://pypi.python.org/pypi/beautifulsoup4-slurp
.. image:: https://img.shields.io/pypi/dm/beautifulsoup4-slurp.svg
        :target: https://pypi.python.org/pypi/beautifulsoup4-slurp
.. image:: https://img.shields.io/pypi/l/beautifulsoup4-slurp.svg
        :target: https://pypi.python.org/pypi/beautifulsoup4-slurp
