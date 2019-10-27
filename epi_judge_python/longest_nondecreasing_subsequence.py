from test_framework import generic_test


def longest_nondecreasing_subsequence_length(A):
    lens = [0] * len(A)
    for i in range(len(A)):
        lens[i] = 1 + max((lens[j]
                           for j in range(i) if A[j] <= A[i]), default=0)
    return max(lens)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_nondecreasing_subsequence.py",
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
