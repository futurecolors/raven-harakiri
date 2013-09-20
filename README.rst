Raven harakiri
==============

UWSGI allows logging `python tracebacks`_ when worker commits harakiri.
This packages sends them to your `sentry`_ instance.

.. _python tracebacks: http://uwsgi-docs.readthedocs.org/en/latest/Tracebacker.html
.. _sentry: http://getsentry.com

Installation
------------
::

    pip install raven-harakiri


Usage
-----

    raven-harakiri <uwsgi_log_string_with_harakiri> --dsn=<your_sentry_dsn>

First argument (or stdin from other process, if piped) should be text with python tracebacker log.
