django-slowtests
========================

.. image:: https://img.shields.io/travis/realpython/django-discover-slowest-tests-runner.svg
    :target: https://travis-ci.org/realpython/django-discover-slowest-tests-runner

.. image:: https://img.shields.io/coveralls/realpython/django-discover-slowest-tests-runner.svg
    :target: https://coveralls.io/r/realpython/django-discover-slowest-tests-runner

.. image:: https://img.shields.io/pypi/dm/django-slowtests.svg
    :target:  https://pypi.python.org/pypi/django-slowtests/

.. image:: https://img.shields.io/pypi/v/django-slowtests.svg
    :target:  https://pypi.python.org/pypi/django-slowtests/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target:  https://pypi.python.org/pypi/django-slowtests/

*Code tested on Django 1.5.12, 1.6.11, 1.7.8, and 1.8.2 with Python 2.7, 3.2, 3.3 3.4.*

Welcome to the documentation for django-slowtests!


Instructions
-----

1. Install::

    $ pip install django-slowtests

2. Add the following setting::

    TEST_RUNNER = 'django_slowtests.DiscoverSlowestTestsRunner'

3. Run test suite::

    ./manage.py test

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

    python setup.py test

or::

    make test

or::

    make all

or::

    python runtests.py


License
-------

This code is distributed under the terms of the MIT license. See the `LICENSE` file.
