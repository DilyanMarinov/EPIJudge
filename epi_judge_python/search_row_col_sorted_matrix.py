from test_framework import generic_test

def matrix_search(A, x):
    i = 0
    j = len(A[0]) - 1
    while i < len(A) and j >= 0:
        if A[i][j] < x:
            i += 1
        elif A[i][j] > x:
            j -= 1
        else:
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
