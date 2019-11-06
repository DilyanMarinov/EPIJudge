from test_framework import generic_test
import re

def is_palindrome(s):
    if len(s) == 1:
        return True
    i = 0
    j = len(s) - 1
    while i <= j:
        while re.match('[\W_]', s[i]):
            i += 1
        while re.match('[\W_]', s[j]):
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_palindromic_punctuation.py",
                                       "is_string_palindromic_punctuation.tsv",
                                       is_palindrome))
