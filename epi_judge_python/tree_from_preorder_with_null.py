import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

class BinaryTreeNode():

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def reconstruct_preorder(preorder):
    return reconstruct_rec(iter(preorder))


def reconstruct_rec(iterator):
    value = next(iterator)
    if value == None:
        return None

    left = reconstruct_rec(iterator)
    right = reconstruct_rec(iterator)
    return BinaryTreeNode(value, left, right)


@enable_executor_hook
def reconstruct_preorder_wrapper(executor, data):
    data = [None if x == 'null' else int(x) for x in data]
    return executor.run(functools.partial(reconstruct_preorder, data))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_with_null.py",
                                       'tree_from_preorder_with_null.tsv',
                                       reconstruct_preorder_wrapper))
