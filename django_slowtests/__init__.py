from django.core.exceptions import ImproperlyConfigured

try:
    from testrunner import DiscoverSlowestTestsRunner  # NOQA
except (ImportError, ImproperlyConfigured):
    pass

__version__ = "0.5.1"
