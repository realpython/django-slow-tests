import time
import operator

from unittest import TestSuite
from django.test.runner import DiscoverRunner
from django.conf import settings


TIMINGS = {}
NUM_SLOW_TESTS = getattr(settings, 'NUM_SLOW_TESTS', 10)


def time_it(func):

    def _timer(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()

        TIMINGS[str(func)] = end_time - start_time

    return _timer


class TimingSuite(TestSuite):
    """
    TestSuite wrapper that times each test.
    """

    def addTest(self, test):
        test = time_it(test)
        super(TimingSuite, self).addTest(test)


class DiscoverSlowestTestsRunner(DiscoverRunner):
    """
    Runner that extends Django's DiscoverRunner to time the tests.
    """

    def build_suite(self, test_labels, extra_tests=None, **kwargs):
        suite = super(DiscoverSlowestTestsRunner, self).build_suite(
            test_labels, extra_tests=extra_tests, **kwargs
        )
        return TimingSuite(suite)

    def teardown_test_environment(self, **kwargs):
        super(DiscoverSlowestTestsRunner, self).teardown_test_environment(**kwargs)
        by_time = sorted(
            iter(TIMINGS.items()),
            key=operator.itemgetter(1),
            reverse=True
        )[:NUM_SLOW_TESTS]
        print("\n%s slowest tests:" % NUM_SLOW_TESTS)
        for func_name, timing in by_time:
            print(("{t:.4f}s {f}".format(f=func_name, t=timing)))
