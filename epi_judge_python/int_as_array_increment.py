from test_framework import generic_test

def plus_one(A):
    carry = 0
    result = A[-1] + 1
    A[-1] = result % 10 + carry
    carry = result // 10
    for i in range(len(A) - 2, -1, -1):
        if carry == 0:
            break
        result = A[i] + carry
        A[i] = result % 10
        carry = result // 10
    if carry == 1:
        A.insert(0, 1)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))
