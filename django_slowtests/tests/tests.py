from django.test import TestCase
from unittest import TestResult
from ..testrunner import TimingSuite, TIMINGS


class TimingSuiteTests(TestCase):

    def setUp(self):
        TIMINGS.clear()

    def test_add_a_test(self):
        from .fake import FakeTestCase
        suite = TimingSuite()
        result = TestResult()
        suite.addTest(FakeTestCase('test_slow_thing'))
        suite.addTest(FakeTestCase('test_setup_class_was_run'))
        suite.run(result)
        self.assertEquals(len(suite._tests), 2)
        self.assertEquals(len(result.errors), 0)

    def test_timing_is_correct_when_freezegun_sets_time_in_past(self):
        from .fake import FakeFrozenInPastTestCase
        suite = TimingSuite()
        result = TestResult()
        suite.addTest(FakeFrozenInPastTestCase('test_this_should_not_have_a_negative_duration'))
        suite.run(result)
        test_name = str(suite._tests[0])
        self.assertTrue(TIMINGS[test_name] > 0)
        self.assertTrue(TIMINGS[test_name] < 1)

    def test_timing_is_correct_when_freezegun_sets_time_in_future(self):
        from .fake import FakeFrozenInFutureTestCase
        suite = TimingSuite()
        result = TestResult()
        suite.addTest(FakeFrozenInFutureTestCase('test_this_should_not_have_very_long_duration'))
        suite.run(result)
        test_name = str(suite._tests[0])
        self.assertTrue(TIMINGS[test_name] > 0)
        self.assertTrue(TIMINGS[test_name] < 1)
