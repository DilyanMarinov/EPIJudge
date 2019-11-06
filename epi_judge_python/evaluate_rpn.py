from test_framework import generic_test


def evaluate(expression):
    values = expression.split(',')
    results = []
    for value in values:
        if value.isdigit():
            results.append(value)
        else:
            second = results.pop()
            first = results.pop()
            results.append(perform_op(int(first), int(second), value))
    return int(results[-1])

def perform_op(first, second, op):
    if op == '+':
        return first + second
    elif op == '-':
        return first - second
    elif op == '*':
        return first * second
    elif op == '/':
        return first // second
    return ''
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
