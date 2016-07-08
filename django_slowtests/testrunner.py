import time
import operator

from unittest import TestSuite, TestLoader
from unittest.suite import _isnotsuite
from django.test.runner import DiscoverRunner
from django.conf import settings


TIMINGS = {}
NUM_SLOW_TESTS = getattr(settings, 'NUM_SLOW_TESTS', 10)


class TimingSuite(TestSuite):
    """
    TestSuite wrapper that times each test.
    """

    def run(self, result, debug=False):
        topLevel = False
        if getattr(result, '_testRunEntered', False) is False:
            result._testRunEntered = topLevel = True

        for test in self:
            if result.shouldStop:
                break

            start_time = time.time()

            if _isnotsuite(test):
                self._tearDownPreviousClass(test, result)
                self._handleModuleFixture(test, result)
                self._handleClassSetUp(test, result)
                result._previousTestClass = test.__class__

                if (getattr(test.__class__, '_classSetupFailed', False) or
                        getattr(result, '_moduleSetUpFailed', False)):
                    continue

            if not debug:
                test(result)
            else:
                test.debug()

            TIMINGS[str(test)] = time.time() - start_time

        if topLevel:
            self._tearDownPreviousClass(None, result)
            self._handleModuleTearDown(result)
            result._testRunEntered = False

        return result


class TimingLoader(TestLoader):
    suiteClass = TimingSuite


class DiscoverSlowestTestsRunner(DiscoverRunner):
    """
    Runner that extends Django's DiscoverRunner to time the tests.
    """
    test_suite = TimingSuite
    test_loader = TimingLoader()

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
