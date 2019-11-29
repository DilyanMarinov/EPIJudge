import functools
from collections import deque
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []

def is_any_placement_feasible(graph):

    def bfs(start):
        q = deque()
        start.d = 0
        q.append(start)
        while len(q) > 0:
            node = q.popleft()
            for n in node.edges:
                if n.d == -1:
                    n.d = node.d + 1
                    q.append(n)
                elif n.d == node.d:
                    return False
        return True

    for node in graph:
        if node.d == -1 and not bfs(node):
            return False
    return True

@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_circuit_wirable.py",
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
