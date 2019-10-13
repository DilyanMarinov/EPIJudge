from test_framework import generic_test, test_utils
import heapq
def k_largest_in_binary_heap(A, k):
    result = []
    heap = []
    heap.append((-1*A[0], 0))
    heapq.heapify(heap)
    while len(result) < k:
        max_val = heapq.heappop(heap)
        left = 2 * max_val[1] + 1
        right = 2 * max_val[1] + 2
        if left < len(A):
            heapq.heappush(heap, (-1*A[left], left))
        if right < len(A):
            heapq.heappush(heap, (-1*A[right], right))
        result.append(-1 * max_val[0])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_in_heap.py",
            "k_largest_in_heap.tsv",
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
