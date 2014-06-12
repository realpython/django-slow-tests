from django.core.exceptions import ImproperlyConfigured

try:
    from testrunner import DiscoverSlowestTestsRunner
except (ImportError, ImproperlyConfigured):
    pass
