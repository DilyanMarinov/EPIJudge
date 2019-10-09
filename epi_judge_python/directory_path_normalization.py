from test_framework import generic_test
import re

def shortest_equivalent_path(path):
    stack = re.split("/+", path)
    stack.reverse()
    result = []
    while len(stack) > 0:
        if stack[-1] == '.' or stack[-1] == '':
            stack.pop()
        elif stack[-1] == '..':
            token = stack.pop()
            if len(result) == 0:
                result.append(token)
            elif result[-1] == '..':
                result.append(token)
            else:
                result.pop()
        else:
            result.append(stack.pop())
    output = '/'.join(result)
    if path[0] == '/':
        output = '/' + output
    return output

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
