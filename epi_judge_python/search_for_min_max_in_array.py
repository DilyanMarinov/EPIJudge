import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def min_max(a, b):
    return MinMax(a, b) if a < b else MinMax(b, a)


def find_min_max(A):

    if len(A) == 1:
        return MinMax(A[0], A[0])

    global_values = min_max(A[0], A[1])
    for i in range(2, len(A) - 1, 2):
        local_values = min_max(A[i], A[i + 1])
        global_values = MinMax(min(local_values.smallest, global_values.smallest), max(local_values.largest, global_values.largest))
    if len(A) % 2:
        global_values = MinMax(min(A[-1], global_values.smallest), max(A[-1], global_values.largest))
    return global_values


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_for_min_max_in_array.py",
            'search_for_min_max_in_array.tsv',
            find_min_max,
            res_printer=res_printer))
