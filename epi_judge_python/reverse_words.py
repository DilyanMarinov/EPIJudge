import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def reverse_words(s):
    reverse_range(s, 0, len(s) - 1)
    start = 0
    finish = 0
    while finish < len(s):
        while finish < len(s) and s[finish] != 32:
            finish += 1
        reverse_range(s, start, finish - 1)
        finish += 1
        start = finish


def reverse_range(b, i, j):
    mid = i + (j - i)//2
    while i <= mid and j >= mid:
        b[i], b[j] = b[j], b[i]
        i += 1
        j -= 1


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
