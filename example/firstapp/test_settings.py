from firstapp.settings import *

# Custom test runner
TEST_RUNNER = 'testrunner.DiscoverSlowestTestsRunner'

# Use an alternative database to safeguard against accidents
DATABASES['default']['NAME'] = '_test.db'