try:
    from django.core.exceptions import ImproperlyConfigured
except ImportError:
    class ImproperlyConfigured(Exception):
        pass

try:
    from testrunner import DiscoverSlowestTestsRunner  # NOQA
except (ImportError, ImproperlyConfigured):
    pass

__version__ = "1.0.2"
