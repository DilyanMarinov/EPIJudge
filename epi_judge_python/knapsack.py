import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    prev = [0] * (capacity + 1)
    cur = [0] * (capacity + 1)
    for i in range(len(items)):
        for j in range(1, capacity + 1):
            if items[i].weight <= j:
                cur[j] = max(prev[j], items[i].value +
                             prev[j - items[i].weight])
            else:
                cur[j] = prev[j]
        temp = prev
        prev = cur
        cur = temp
    return prev[-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
