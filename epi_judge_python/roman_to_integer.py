from test_framework import generic_test

def roman_to_integer(s):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    special = {'V': ('I', 4), 'X': ('I', 9), 'L': ('X', 40),
                'C': ('X', 90), 'D': ('C', 400), 'M': ('C', 900)}
    result = 0
    i = len(s) - 1
    while i > 0:
        if s[i] in special and special[s[i]][0] == s[i - 1]:
            result += special[s[i]][1]
            i -= 2
        else:
            result += values[s[i]]
            i -= 1
    if i == 0:
        result += values[s[0]]
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
