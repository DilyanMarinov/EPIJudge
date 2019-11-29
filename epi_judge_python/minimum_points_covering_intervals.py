import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))

def find_minimum_visits(intervals):
    if len(intervals) == 0:
        return 0
    def getKey(interval):
        return interval.right
    intervals.sort(key=getKey)
    current = intervals[0].right
    points = [intervals[0].right]
    for interval in intervals:
        if current >= interval.left and current <= interval.right:
            continue
        else:
            points.append(interval.right)
            current = interval.right
    print(points)
    return len(points)


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_points_covering_intervals.py",
                                       'minimum_points_covering_intervals.tsv',
                                       find_minimum_visits_wrapper))
