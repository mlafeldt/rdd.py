rdd.py
======

rdd.py is a Python implementation of the [Readability Shortener API].

The project comes with a Python module that can be imported via `import rdd` and
a simple command-line tool named `rdd` to utilize it.


Installation
------------

rdd.py requires [Requests]. [This page][Requests-install] explains how to
install it.

rdd.py itself can be installed via `setup.py`:

    $ git clone git://github.com/mlafeldt/rdd.py.git
    $ cd rdd.py/
    $ python setup.py install

Alternatively, you can use pip:

    $ pip install git+git://github.com/mlafeldt/rdd.py.git


API Usage
---------

```python
>>> import rdd

>>> readability = rdd.Readability()

>>> readability.resources()
{'urls/:id': {'description': 'The URL endpoint. GET a URL ID to view available metadata of a shortened link.', 'href': '/api/shortener/v1/urls/:id'}, 'urls': {'description': 'The URLs endpoint. POST a URL to add it to the shortener.', 'href': '/api/shortener/v1/urls'}}

>>> readability.shorten('http://www.paulgraham.com/gh.html')
{'url': '/api/shortener/v1/urls/ga4qf47t', 'id': 'ga4qf47t', 'rdd_url': 'http://rdd.me/ga4qf47t'}

>>> readability.metadata('ga4qf47t')
{'id': 'ga4qf47t', 'rdd_url': 'http://rdd.me/ga4qf47t', 'article': {'url': 'http://www.paulgraham.com/gh.html', 'word_count': 5147, 'excerpt': 'Want to start a startup? Get funded by Y Combinator. July 2004(This essay is derived from a talk at Oscon 2004.)A few months ago I finished a new book, and in reviews I keep noticing words like&hellip;', 'author': None, 'title': 'Great Hackers'}, 'full_url': 'http://readability.com/articles/ga4qf47t'}
```


Client Usage
------------

See [rdd(1)] manual page for the ins and outs of the `rdd` tool.


Testing
-------

[![Build Status](https://travis-ci.org/mlafeldt/rdd.py.png?branch=master)](https://travis-ci.org/mlafeldt/rdd.py)

rdd.py comes with both unit and integration tests.

You can run the tests this way:

    $ python setup.py test             # Runs the entire test suite.
    $ python setup.py test_units       # Runs all unit tests.
    $ python setup.py test_integration # Runs all integration tests.



License
-------

* rdd.py is licensed under the terms of the MIT License. See [LICENSE] file.
* [Sharness] and all integration tests are licensed under the terms of the GNU
  General Public License version 2 or higher. See file [COPYING] for full license
  text.


Contact
-------

* Web: <http://mlafeldt.github.com/rdd.py>
* Mail: <mathias.lafeldt@gmail.com>
* Twitter: [@mlafeldt](https://twitter.com/mlafeldt)


[COPYING]: https://github.com/mlafeldt/rdd.py/blob/master/test/COPYING
[LICENSE]: https://github.com/mlafeldt/rdd.py/blob/master/LICENSE
[Readability Shortener API]: https://www.readability.com/developers/api/rdd
[Sharness]: https://github.com/mlafeldt/Sharness
[rdd(1)]: http://mlafeldt.github.com/rdd.py/man/rdd.1.html
[Requests]: http://python-requests.org
[Requests-install]: http://docs.python-requests.org/en/latest/user/install/
