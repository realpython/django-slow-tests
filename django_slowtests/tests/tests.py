from django.test import TestCase
from mock import patch
from unittest import TestResult
from ..testrunner import TimingSuite


class TimingSuiteTests(TestCase):
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
        with patch.object(suite, 'save_test_time') as mock:
            suite.run(result)
        test_name = str(suite._tests[0])
        mock.assert_called_once()
        self.assertEqual(mock.call_args_list[0][0][0], test_name)
        self.assertTrue(mock.call_args_list[0][0][1] > 0)
        self.assertTrue(mock.call_args_list[0][0][1] < 1)

    def test_timing_is_correct_when_freezegun_sets_time_in_future(self):
        from .fake import FakeFrozenInFutureTestCase
        suite = TimingSuite()
        result = TestResult()
        suite.addTest(FakeFrozenInFutureTestCase('test_this_should_not_have_very_long_duration'))
        with patch.object(suite, 'save_test_time') as mock:
            suite.run(result)
        test_name = str(suite._tests[0])
        self.assertEqual(mock.call_args_list[0][0][0], test_name)
        self.assertTrue(mock.call_args_list[0][0][1] > 0)
        self.assertTrue(mock.call_args_list[0][0][1] < 1)
