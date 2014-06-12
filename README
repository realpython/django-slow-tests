# Django DiscoverSlowestTestsRunner

Code tested on Django 1.6.5 with Python 2.7 and 3.4.

## Setup

1. Install: `pip install django-slowtests`
2. Add the following setting: `TEST_RUNNER = 'django-slowtests.DiscoverSlowestTestsRunner'`

## Run test suite

```bash
./manage.py test
```

## Sample output

```bash
$ python manage.py test
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

## License

This code is distributed under the terms of the MIT license. See the `LICENSE` file.
