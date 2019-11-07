from test_framework import generic_test, test_utils

def generate_power_set(S):
    holder = []
    generate_set(S, [], holder, 0)
    return holder

def generate_set(S, current, holder, j):
    holder.append(current[:])
    for i in range(j, len(S)):
        current.append(S[i])
        generate_set(S, current, holder, i + 1)
        del current[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
