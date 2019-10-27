from test_framework import generic_test
from bitarray import bitarray

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment):
    rows = len(partial_assignment)
    columns = len(partial_assignment[0])
    valid = bitarray(columns)
    for i in range(rows):
        valid.setall(0)
        for j in range(columns):
            if partial_assignment[i][j] != 0:
                if valid[partial_assignment[i][j] - 1] == 0:
                    valid[partial_assignment[i][j] - 1] = 1
                else:
                    return False

    for i in range(columns):
        valid.setall(0)
        for j in range(rows):
            if partial_assignment[j][i] != 0:
                if valid[partial_assignment[j][i] - 1] == 0:
                    valid[partial_assignment[j][i] - 1] = 1
                else:
                    return False

    for i in range(0, rows, 3):
        for j in range(0, columns, 3):
            valid.setall(0)
            if not check_quad(partial_assignment, i, j, valid):
                return False
    return True


def check_quad(A, starti, startj, valid):
    for i in range(starti, starti + 3):
        for j in range(startj, startj + 3):
            if A[i][j] != 0:
                if valid[A[i][j] - 1] == 0:
                    valid[A[i][j] - 1] = 1
                else:
                    return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
