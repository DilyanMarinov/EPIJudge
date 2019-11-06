from test_framework import generic_test

class Node(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)


def binary_tree_from_preorder_inorder(preorder, inorder):
    if len(inorder) == 0:
        return
    root = Node(preorder[0])
    index = inorder.index(root.data)
    del preorder[0]
    root.left = binary_tree_from_preorder_inorder(preorder, inorder[0:index])
    root.right = binary_tree_from_preorder_inorder(preorder, inorder[index + 1:])
    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
