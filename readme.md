# Django DiscoverSlowestTestsRunner

Code Tested with Django 1.6.5.

## Setup

1. Add *testrunner.py* to the Project Root
2. Add the contents of *test_settings.py* to the directory containing the *settings.py* file.

## Run test suite

```bash
./manage.py test --settings=project_name.test_settings
```

## Sample output

```bash
$ python manage.py test --settings=firstapp.test_settings
Creating test database for alias 'default'...
..........
----------------------------------------------------------------------
Ran 10 tests in 0.413s

OK
Destroying test database for alias 'default'...

Ten slowest tests:
0.3597s test_detail_view_with_a_future_poll (polls.tests.PollIndexDetailTests)
0.0284s test_detail_view_with_a_past_poll (polls.tests.PollIndexDetailTests)
0.0068s test_index_view_with_a_future_poll (polls.tests.PollViewTests)
0.0047s test_index_view_with_a_past_poll (polls.tests.PollViewTests)
0.0045s test_index_view_with_two_past_polls (polls.tests.PollViewTests)
0.0041s test_index_view_with_future_poll_and_past_poll (polls.tests.PollViewTests)
0.0036s test_index_view_with_no_polls (polls.tests.PollViewTests)
0.0003s test_was_published_recently_with_future_poll (polls.tests.PollMethodTests)
0.0002s test_was_published_recently_with_recent_poll (polls.tests.PollMethodTests)
0.0002s test_was_published_recently_with_old_poll (polls.tests.PollMethodTests)
```
