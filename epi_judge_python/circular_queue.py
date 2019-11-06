from test_framework import generic_test
from test_framework.test_failure import TestFailure

class Queue:
    def __init__(self, capacity):
        self.q = [0]*capacity
        self.head = self.tail = self.total = 0
    def enqueue(self, x):
        if self.total == len(self.q):
            self.q = (self.q[self.head:] + self.q[:self.head])
            self.head = 0
            self.tail = self.total
            self.q.extend([0] * (2 * len(self.q)))
        self.q[self.tail] = x
        self.tail = (self.tail + 1) % len(self.q)
        self.total += 1

    def dequeue(self):
        self.total -= 1
        result = self.q[self.head]
        self.head = (self.head + 1) % len(self.q)
        return result

    def size(self):
        return self.total


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
