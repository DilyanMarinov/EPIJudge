from test_framework import generic_test

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L, k):
    first = L
    second = L
    count = 0
    while count <= k and first != None:
        first = first.next
        count += 1
    if first == None and count <= k:
        L = L.next
        return L
    while first != None:
        first = first.next
        second = second.next
    second.next = second.next.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
