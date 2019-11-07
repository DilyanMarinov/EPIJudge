from test_framework import generic_test, test_utils

def permutations(A):
    perms = []
    permute(A, 0, len(A), perms)
    return perms


def permute(A, i, j, perms):
    if i == j - 1:
        perms.append(A[:])
    for k in range(i, j):
        A[i], A[k] = A[k], A[i]
        permute(A, i + 1, j, perms)
        A[i], A[k] = A[k], A[i]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
