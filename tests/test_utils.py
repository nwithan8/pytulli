from datetime import datetime

from tautulli.internal.utils import (
    datetime_to_string
)

def test_datetime_to_string():
    date = datetime(2021, 1, 1, 0, 0, 0)

    # default format: "%Y-%m-%d"
    assert datetime_to_string(datetime_object=date) == "2021-01-01"

    fmt = "%Y-%m-%d %H:%M:%S"
    assert datetime_to_string(datetime_object=date, string_format=fmt) == "2021-01-01 00:00:00"
