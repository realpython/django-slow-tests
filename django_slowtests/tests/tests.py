from django.test import TestCase
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
