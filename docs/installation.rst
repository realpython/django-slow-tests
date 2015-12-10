.. _installation:

============
Installation
============

* Install the development version::

    pip install django-slowtests

* Add the following setting::

    # Custom test runner
    TEST_RUNNER = 'django_slowtests.testrunner.DiscoverSlowestTestsRunner'
    NUM_SLOW_TESTS = 10



.. _dependencies:

Dependencies
============

