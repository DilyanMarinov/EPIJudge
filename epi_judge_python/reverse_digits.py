from test_framework import generic_test
from math import floor, log10

def reverse(x):
    if x == 0:
        return 0
    num = abs(x)
    digits = floor(log10(num)) + 1
    result = 0
    for i in range(1, digits + 1):
        coef = (num % 10 ** i) // 10 ** (i - 1)
        result += coef * 10**(digits-i)

    if x < 0:
        return result*-1
    else:
        return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
