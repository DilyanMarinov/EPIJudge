from test_framework import generic_test

def get_max_trapped_water(heights):
    i = 0
    j = len(heights) - 1
    maxvol = 0
    while j > i:
        maxvol = max(maxvol, (j - i) * min(heights[i], heights[j]))
        if heights[i] < heights[j]:
            i += 1
        elif heights[j] < heights[i]:
            j -= 1
        else:
            i += 1
            j -= 1
    return maxvol


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))
