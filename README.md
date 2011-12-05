rdd.py
======

rdd.py is a Python implementation of the [Readability Shortener API].

rdd.py comes with a Python module that can be imported via `import rdd` and a
simple command-line tool named `rdd` to utilize it.


Installation
------------

rdd.py requires [Requests] -- the excellent HTTP library by Kenneth Reitz
(@kennethreitz). [This page][Requests-install] explains how to install it.

rdd.py itself can be installed via `setup.py`:

```sh
$ python setup.py install
```


Client Usage
------------

(See [rdd(1)] manpage for more information.)

Retrieve information about sub-resources:

```sh
$ rdd resources
{
    "resources": {
        "urls/:id": {
            "href": "/api/shortener/v1/urls/:id",
            "description": "The URL endpoint. GET a URL ID to view available metadata of a shortened link."
        },
        "urls": {
            "href": "/api/shortener/v1/urls",
            "description": "The URLs endpoint. POST a URL to add it to the shortener."
        }
    }
}
```

Create a new shortened URL:

```sh
$ rdd shorten http://www.paulgraham.com/gh.html
{
    "meta": {
        "url": "/api/shortener/v1/urls/ga4qf47t",
        "rdd_url": "http://rdd.me/ga4qf47t",
        "id": "ga4qf47t"
    },
    "messages": [
        "URL shortened."
    ],
    "success": true
}
```

Retrieve available metadata of a shortened link:

```sh
$ rdd metadata ga4qf47t
{
    "meta": {
        "article": {
            "url": "http://www.paulgraham.com/gh.html",
            "title": "Great Hackers",
            "excerpt": "Want to start a startup? Get funded by Y Combinator . July 2004 (This essay is derived from a talk at Oscon 2004.) A few months ago I finished a new book , and in reviews I keep noticing words like&hellip;",
            "word_count": 5147,
            "author": null
        },
        "rdd_url": "http://rdd.me/ga4qf47t",
        "id": "ga4qf47t",
        "full_url": "http://readability.com/articles/ga4qf47t"
    },
    "messages": [
        "Article found."
    ],
    "success": true
}
```


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


Automated Tests
---------------

The `test` folder contains some automated test scripts powered by [Sharness].

You can run the tests this way:

```sh
$ make -C test/
*** t0001-resources.sh ***
ok 1 - Get information about sub-resources
# passed all 1 test(s)
1..1
*** t0002-shorten.sh ***
ok 1 - Shorten URL http://www.paulgraham.com/gh.html (ga4qf47t)
ok 2 - Shorten URL http://the99percent.com/articles/6943/What-Motivates-Us-To-Do-Great-Work (75x8oaqg)
ok 3 - Shorten URL http://www.inc.com/magazine/20100401/driven-to-distraction.html (yibs1cca)
# passed all 3 test(s)
1..3
*** t0003-metadata.sh ***
ok 1 - Get metadata of ga4qf47t (http://www.paulgraham.com/gh.html)
ok 2 - Get metadata of 75x8oaqg (http://the99percent.com/articles/6943/What-Motivates-Us-To-Do-Great-Work)
ok 3 - Get metadata of yibs1cca (http://www.inc.com/magazine/20100401/driven-to-distraction.html)
# passed all 3 test(s)
1..3

fixed   0
success 7
failed  0
broken  0
total   7
```


License
-------

* rdd.py is licensed under the terms of the MIT License. See [LICENSE] file.
* [Sharness] and all tests are licensed under the terms of the GNU General
  Public License version 2 or higher. See file [COPYING] for full license text.


Contact
-------

* Web: <https://github.com/mlafeldt/rdd.py>
* Mail: <mathias.lafeldt@gmail.com>


[COPYING]: https://github.com/mlafeldt/rdd.py/blob/master/test/COPYING
[LICENSE]: https://github.com/mlafeldt/rdd.py/blob/master/LICENSE
[Readability Shortener API]: https://www.readability.com/publishers/rdd
[Sharness]: https://github.com/mlafeldt/Sharness
[rdd(1)]: http://mlafeldt.github.com/rdd.py/rdd.1.html
[Requests]: http://python-requests.org
[Requests-install]: http://docs.python-requests.org/en/latest/user/install/
