from test_framework import generic_test, test_utils

def generate_balanced_parentheses(num_pairs):
    result = []
    gen_rec(num_pairs, num_pairs, '', result)
    return result

def gen_rec(left_needed, right_needed, prefix, result):

    if left_needed > 0:
        gen_rec(left_needed - 1, right_needed, prefix + '(', result)

    if left_needed < right_needed:
        gen_rec(left_needed, right_needed - 1, prefix + ')', result)

    if right_needed == 0:
        result.append(prefix)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
