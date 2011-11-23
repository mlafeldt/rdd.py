rdd.py
======

rdd.py is a Python implementation of the [Readability Shortener API].

rdd.py comes with a Python module that can be imported via ```import rdd``` and
a simple command-line tool named ```rdd``` to utilize it.


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


License
-------

See [LICENSE] file.


Contact
-------

* Web: <https://github.com/mlafeldt/rdd.py>
* Mail: <mathias.lafeldt@gmail.com>


[Readability Shortener API]: https://www.readability.com/publishers/rdd
[LICENSE]: https://github.com/mlafeldt/rdd.py/blob/master/LICENSE
[rdd(1)]: http://mlafeldt.github.com/rdd.py/rdd.1.html
