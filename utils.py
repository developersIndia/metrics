import time
from datetime import datetime, timedelta
from sys import platform


def non_zero_padded_prefix():
    """Returns the platform specific prefix for the non-zero-padded numbers."""
    prefix = "-"
    if platform.startswith("win32"):
        prefix = "#"

    return prefix


def get_last_month() -> str:
    now = datetime.now()
    last_month = now - timedelta(weeks=4)
    return last_month.strftime(f"%{non_zero_padded_prefix()}m %Y")


def get_last_day() -> str:
    now = datetime.now()
    last_day = now - timedelta(days=1)
    return last_day.strftime(f"%d/%{non_zero_padded_prefix()}m/%Y")


def get_readable_month(unix_t: float) -> str:
    t = time.localtime(unix_t)
    # Format: '9, 2021'
    return time.strftime(f"%{non_zero_padded_prefix()}m %Y", t)


def get_readable_day(unix_t: float) -> str:
    t = time.localtime(unix_t)
    # Format: '03/12/2021'
    return time.strftime(f"%d/%{non_zero_padded_prefix()}m/%Y", t)
