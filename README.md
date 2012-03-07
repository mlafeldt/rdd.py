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
    $ cd rdd.py
    $ python setup.py install


Client Usage
------------

See [rdd(1)] manual page for the ins and outs of the `rrd` tool.


API Usage
---------

```python
>>> import rdd
>>> readability = rdd.Readability()
>>> readability.resources()
{u'resources': {u'urls/:id': {u'href': u'/api/shortener/v1/urls/:id', u'description': u'The URL endpoint. GET a URL ID to view available metadata of a shortened link.'}, u'urls': {u'href': u'/api/shortener/v1/urls', u'description': u'The URLs endpoint. POST a URL to add it to the shortener.'}}}
>>> readability.shorten('http://www.paulgraham.com/gh.html')
{'meta': {'url': '/api/shortener/v1/urls/ga4qf47t', 'rdd_url': 'http://rdd.me/ga4qf47t', 'id': 'ga4qf47t'}, 'messages': ['URL shortened.'], 'success': True}
>>> readability.metadata('ga4qf47t')
{'meta': {'article': {'url': 'http://www.paulgraham.com/gh.html', 'title': 'Great Hackers', 'excerpt': 'Want to start a startup? Get funded by Y Combinator . July 2004 (This essay is derived from a talk at Oscon 2004.) A few months ago I finished a new book , and in reviews I keep noticing words like&hellip;', 'word_count': 5147, 'author': None}, 'rdd_url': 'http://rdd.me/ga4qf47t', 'id': 'ga4qf47t', 'full_url': 'http://readability.com/articles/ga4qf47t'}, 'messages': ['Article found.'], 'success': True}
```


Tests
-----

The `test` folder contains some automated test scripts powered by [Sharness].

You can run the tests this way:

    $ make -C test


License
-------

* rdd.py is licensed under the terms of the MIT License. See [LICENSE] file.
* [Sharness] and all tests are licensed under the terms of the GNU General
  Public License version 2 or higher. See file [COPYING] for full license text.


Contact
-------

* Web: <https://github.com/mlafeldt/rdd.py>
* Mail: <mathias.lafeldt@gmail.com>
* Twitter: [@mlafeldt](https://twitter.com/mlafeldt)


[COPYING]: https://github.com/mlafeldt/rdd.py/blob/master/test/COPYING
[LICENSE]: https://github.com/mlafeldt/rdd.py/blob/master/LICENSE
[Readability Shortener API]: https://www.readability.com/publishers/rdd
[Sharness]: https://github.com/mlafeldt/Sharness
[rdd(1)]: http://mlafeldt.github.com/rdd.py/rdd.1.html
[Requests]: http://python-requests.org
[Requests-install]: http://docs.python-requests.org/en/latest/user/install/
