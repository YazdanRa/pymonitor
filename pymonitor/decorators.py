import functools
from datetime import datetime

from .templates import time_result


def monitor(measure):
    def time_monitor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            func(*args, **kwargs)
            end_time = datetime.now()

            print(time_result.format(
                start_time=start_time.time(),
                end_time=end_time.time(),
                process_time=end_time - start_time,
            ))

        return wrapper

    monitor_map = dict(
        time=time_monitor,
    )

    if measure not in monitor_map.keys():
        raise AssertionError(
            f"'{measure}' is not a valid measure! "
            f"Please choose a correct measure: {list(monitor_map.keys())}"
        )

    return monitor_map[measure]
