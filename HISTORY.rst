History
-------

0.1.7 (2012-06-07)
++++++++++++++++++

* Make use of ``Response.json`` from Requests v0.12.1.
* Add Python 3 support.
* Add Travis CI config, testing Python 2.6, 2.7, and 3.2.
* Update to Sharness v0.2.1.

0.1.6 (2012-02-09)
++++++++++++++++++

* Fix URL of shortener service. For whatever reason, HTTPS is no longer
  supported. Only http://www.readability.com/api/shortener/v1 works.
* Disable annoying HTTP POST redirection.

0.1.5 (2012-01-18)
++++++++++++++++++

* Add more automated tests.
* Fix tests to pass on Mac OS X Lion.
* Set ``RDD_VERBOSE`` with test option -v.

0.1.4 (2011-12-05)
++++++++++++++++++

* Support environment variables ``RDD_URL`` and ``RDD_VERBOSE``.
* Additionally print HTTP content in verbose mode.
* Add rdd.exceptions (imports exceptions from Requests).
* Improve documentation (install instructions, docstrings, etc.)

0.1.3 (2011-12-04)
++++++++++++++++++

* Add automated tests powered by Sharness.

0.1.2 (2011-11-23)
++++++++++++++++++

* Split up rdd.py into package and runner script.
* Add setup.py for easy installation.

0.1.1 (2011-11-22)
++++++++++++++++++

* Add ``--url`` option.
* Allow HTTP redirects.
* Import ``json`` if ``simplejson`` is not available.
* Add ``__author__``, ``__license__``, and ``__version__``.
* Add manpage in ronn format.
* Syntax highlighting in README.
* Add this history file.

0.1.0 (2011-11-21)
++++++++++++++++++

* First version (written on the same day the Readability API was released)
