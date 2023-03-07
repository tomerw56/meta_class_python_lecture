# using time module
import time


class Timer:
    def __init__(self):
        self._start_time=0
    def __enter__(self):
        print('started_time')
        # ts stores the time in seconds
        self._start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('EXIT WITH:', end=' ')
        if exc_type:
            print("Exception handled")
        print(f'worked for {time.time()-self._start_time} seconds')


def strange_long_operation(sleep_time:float):
    time.sleep(sleep_time)
    if sleep_time<1.0:
        raise AssertionError("input no valid")

print("works fine")
with Timer() as t:
    strange_long_operation(sleep_time=2)

print("exception handled")
with Timer() as t:
    strange_long_operation(sleep_time=0.5)