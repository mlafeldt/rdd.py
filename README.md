rdd.py
======

rdd.py is a Python implementation of the [Readability Shortener API].

The project comes with a Python module that can be imported via `import rdd` and
a simple command-line tool named `rdd` to utilize it.


Installation
------------

rdd.py requires [Requests] - the excellent HTTP library by Kenneth Reitz.
[This page][Requests-install] explains how to install it.

rdd.py itself can be installed via `setup.py`:

    $ git clone git://github.com/mlafeldt/rdd.py.git
    $ cd rdd.py/
    $ python setup.py install


API Usage
---------

```python
>>> import rdd

>>> readability = rdd.Readability()

>>> readability.resources()
{u'urls/:id': {u'href': u'/api/shortener/v1/urls/:id', u'description': u'The URL endpoint. GET a URL ID to view available metadata of a shortened link.'}, u'urls': {u'href': u'/api/shortener/v1/urls', u'description': u'The URLs endpoint. POST a URL to add it to the shortener.'}}

>>> readability.shorten('http://www.paulgraham.com/gh.html')
{u'url': u'/api/shortener/v1/urls/ga4qf47t', u'rdd_url': u'http://rdd.me/ga4qf47t', u'id': u'ga4qf47t'}

>>> readability.metadata('ga4qf47t')
{u'article': {u'url': u'http://www.paulgraham.com/gh.html', u'title': u'Great Hackers', u'excerpt': u'Want to start a startup? Get funded by Y Combinator. ...', u'word_count': 5147, u'author': None}, u'rdd_url': u'http://rdd.me/ga4qf47t', u'id': u'ga4qf47t', u'full_url': u'http://readability.com/articles/ga4qf47t'}
```


Client Usage
------------

See [rdd(1)] manual page for the ins and outs of the `rrd` tool.


Tests
-----

[![Build Status](https://travis-ci.org/mlafeldt/rdd.py.png?branch=master)](https://travis-ci.org/mlafeldt/rdd.py)

The `test` folder contains both unit and integration tests.

You can run the unit tests this way:

    $ python setup.py test

And for the integration tests:

    $ make -C test/integration


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
[Readability Shortener API]: https://www.readability.com/publishers/rdd
[Sharness]: https://github.com/mlafeldt/Sharness
[rdd(1)]: http://mlafeldt.github.com/rdd.py/man/rdd.1.html
[Requests]: http://python-requests.org
[Requests-install]: http://docs.python-requests.org/en/latest/user/install/
