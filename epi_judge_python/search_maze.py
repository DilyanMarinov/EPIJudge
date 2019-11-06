from collections import namedtuple
from collections import deque
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = namedtuple('Coordinate', ('x', 'y'))
def search_maze(maze, s, e):
    return search_maze_copy(copy.deepcopy(maze), s, e)

def search_maze_copy(maze, s, e):
    q = deque()
    q.appendleft(s)
    rows = len(maze)
    cols = len(maze[0])
    prev = {(s.x, s.y): None}
    while len(q) > 0:
        current = q.pop()
        maze[current.x][current.y] = BLACK
        i, j = current.x, current.y
        if current.x == e.x and current.y == e.y:
            return reconstruct_path(e,prev)
        if j - 1 >= 0 and maze[i][j - 1] == WHITE:
            q.appendleft(Coordinate(i, j - 1))
            prev[(i, j - 1)] = (current.x, current.y)
        if j + 1 < cols and maze[i][j + 1] == WHITE:
            q.appendleft(Coordinate(i, j + 1))
            prev[(i, j + 1)] = (current.x, current.y)
        if i - 1 >= 0 and maze[i - 1][j] == WHITE:
            q.appendleft(Coordinate(i - 1, j))
            prev[(i - 1, j)] = (current.x, current.y)
        if i + 1 < rows and maze[i + 1][j] == WHITE:
            q.appendleft(Coordinate(i + 1, j))
            prev[(i + 1, j)] = (current.x, current.y)
    return []

def reconstruct_path(end, path):
    result = []
    last = (end.x, end.y)
    while last != None:
        result.append(Coordinate(last[0], last[1]))
        last = path[last]
    result.reverse()
    return result


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
