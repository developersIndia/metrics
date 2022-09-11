import time
import unittest
from datetime import datetime, timedelta
from unittest.mock import patch

from utils import (
    get_last_day,
    get_last_month,
    get_readable_day,
    get_readable_month,
    non_zero_padded_prefix,
)


class TestUtils(unittest.TestCase):
    def setUp(self):
        # wrapping non-mocked attributes
        self.datetime_patcher = patch("utils.datetime", wraps=datetime)
        self.time_patcher = patch("utils.time", wraps=time)
        self.now = datetime.now()  # should we use a specific datetime here instead?
        self.localtime = time.localtime(self.now.timestamp())
        self.datetime_mock = self.datetime_patcher.start()
        self.time_mock = self.time_patcher.start()
        self.datetime_mock.now.return_value = self.now
        self.time_mock.localtime.return_value = self.localtime

    def test_last_month_returns_date_string_four_weeks_from_now(self):
        last_month = self.now - timedelta(weeks=4)
        self.assertEqual(
            last_month.strftime(f"%{non_zero_padded_prefix()}m %Y"), get_last_month()
        )

    def test_get_last_day_returns_yesterdays_date_string(self):
        last_day = self.now - timedelta(days=1)
        self.assertEqual(
            last_day.strftime(f"%d/%{non_zero_padded_prefix()}m/%Y"), get_last_day()
        )

    def test_get_readable_month_returns_date_string_for_current_month(self):
        self.assertEqual(
            time.strftime(f"%{non_zero_padded_prefix()}m %Y", self.localtime),
            get_readable_month(self.now.timestamp()),
        )

    def test_get_readable_day_returns_date_string_for_current_day(self):
        self.assertEqual(
            time.strftime(f"%d/%{non_zero_padded_prefix()}m/%Y", self.localtime),
            get_readable_day(self.now.timestamp()),
        )

    def tearDown(self):
        self.time_patcher.stop()
        self.datetime_patcher.stop()


if __name__ == "__main__":
    unittest.main()
