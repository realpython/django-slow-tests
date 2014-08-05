from django.test import TestCase

from ..testrunner import TimingSuite


class TimingSuiteTests(TestCase):

    def test_add_a_test(self):
        from .fake import FakeTestCase
        suite = TimingSuite()
        suite.addTest(FakeTestCase("test_fake_thing"))
        self.assertEquals(len(suite._tests), 1)
