from test_framework import generic_test
import math

def is_palindrome_number(x):
    if x <= 0:
        return x == 0
    length = math.floor(math.log10(x)) + 1
    for i in range(1, length//2 + 1):
        lsd = (x % 10 ** i)//10 ** (i - 1)
        msd = (x // 10 ** (length - i)) % 10
        if lsd != msd:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
