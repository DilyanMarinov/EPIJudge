from test_framework import generic_test
from sortedcontainers import SortedSet
from math import sqrt


def generate_first_k_a_b_sqrt2(k):
    result = []
    q = sqrt(2)
    tree = SortedSet([(0.0, 0, 0)])
    while len(result) < k:
        smallest = tree.pop(0)
        result.append(smallest[0])
        a = smallest[1]
        b = smallest[2]
        tree.add(((a+1) + b*q, a+1, b))
        tree.add((a + (b+1)*q, a, b+1))
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
