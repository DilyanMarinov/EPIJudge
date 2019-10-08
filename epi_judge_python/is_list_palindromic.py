from test_framework import generic_test

def find_middle(start):
    end = start
    middle = start
    while end != None:
        end = end.next
        if end != None:
            end = end.next
        middle = middle.next
    return middle


def reverse_list(start):
    nextNode = None
    while start != None:
        temp = start.next
        start.next = nextNode
        nextNode = start
        start = temp
    return nextNode


def print_list(start):
    while start != None:
        print(start.data)
        start = start.next


def is_linked_list_a_palindrome(L):
    mid_reversed = reverse_list(find_middle(L))
    while mid_reversed != None:
        if L.data != mid_reversed.data:
            return False
        mid_reversed = mid_reversed.next
        L = L.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_list_palindromic.py",
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
