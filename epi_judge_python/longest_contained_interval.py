from test_framework import generic_test


def longest_contained_range(A):
    numbers = set(A)
    maxCount = 0
    count = 0
    while len(numbers) > 0:
        number = numbers.pop()
        left = number - 1
        right = number + 1
        count += 1
        while left in numbers:
            numbers.remove(left)
            count += 1
            left -= 1
        while right in numbers:
            numbers.remove(right)
            count += 1
            right += 1
        maxCount = max(count, maxCount)
        count = 0
    return maxCount


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
