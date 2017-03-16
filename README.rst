django-slowtests
========================

.. image:: https://travis-ci.org/realpython/django-slow-tests.svg?branch=master
    :target: https://travis-ci.org/realpython/django-slow-tests

.. image:: https://coveralls.io/repos/realpython/django-slow-tests/badge.svg?branch=master
  :target: https://coveralls.io/r/realpython/django-slow-tests?branch=master

.. image:: https://img.shields.io/pypi/v/django-slowtests.svg
    :target:  https://pypi.python.org/pypi/django-slowtests/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target:  https://pypi.python.org/pypi/django-slowtests/

Welcome!
--------

Welcome to the documentation for django-slowtests!

*Code tested on Django 1.6, 1.7, 1.8, 1.9, and 1.10 with Python 2.7 and 3.6.*


Instructions
-------------

1. Install::

    $ pip install django-slowtests

2. Add the following settings::

    TEST_RUNNER = 'django_slowtests.testrunner.DiscoverSlowestTestsRunner'
    NUM_SLOW_TESTS = 10

    # (Optional)
    SLOW_TEST_THRESHOLD_MS = 200  # Only show tests slower than 200ms

3. Run test suite::

    $ python manage.py test

4. Sample output::


    $ python manage.py test
    Creating test database for alias 'default'...
    ..........
    ----------------------------------------------------------------------
    Ran 10 tests in 0.413s

    OK
    Destroying test database for alias 'default'...

    Ten slowest tests:
    0.3597s test_detail_view_with_a_future_poll (polls.tests.PollIndexDetailTests)
    0.0284s test_detail_view_with_a_past_poll (polls.tests.PollIndexDetailTests)
    0.0068s test_index_view_with_a_future_poll (polls.tests.PollViewTests)
    0.0047s test_index_view_with_a_past_poll (polls.tests.PollViewTests)
    0.0045s test_index_view_with_two_past_polls (polls.tests.PollViewTests)
    0.0041s test_index_view_with_future_poll_and_past_poll (polls.tests.PollViewTests)
    0.0036s test_index_view_with_no_polls (polls.tests.PollViewTests)
    0.0003s test_was_published_recently_with_future_poll (polls.tests.PollMethodTests)
    0.0002s test_was_published_recently_with_recent_poll (polls.tests.PollMethodTests)
    0.0002s test_was_published_recently_with_old_poll (polls.tests.PollMethodTests)



Running the Tests
------------------------------------

You can run the tests via::

    $ python setup.py test

or::

    $ make test

or::

    $ make all

or::

    $ python runtests.py


Known Issues
------------



License
-------

This code is distributed under the terms of the MIT license. See the `LICENSE` file.
