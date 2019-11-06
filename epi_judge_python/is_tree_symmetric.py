from test_framework import generic_test

class Node(object):

    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def is_symmetric(tree):
    if not tree:
        return True
    else:
        return sym_both(tree.left, tree.right)
def sym_both(left, right):
    if not left and not right:
        return True
    elif left and right:
        return left.data == right.data and sym_both(left.left, right.right) and sym_both(left.right, right.left)
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))
