import time
from django.test import TestCase


class FakeTestCase(TestCase):
    _setupClassRan = False

    @classmethod
    def setUpClass(cls):
        super(FakeTestCase, cls).setUpClass()
        cls._setupClassRan = True

    def test_slow_thing(self):
        time.sleep(1)

    def test_setup_class_was_run(self):
        self.assertTrue(self._setupClassRan)
