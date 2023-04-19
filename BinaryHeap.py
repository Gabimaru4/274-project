import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree


def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return 2 * i + 1


def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return 2 * (i + 1)


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return (i - 1) // 2


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        if self.n == 0:
            raise IndexError
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self._trickle_down_root()
        if 3 * self.n < len(self.a):
            self._resize()
        return x

    def depth(self, u) -> int:
        for i in range(self.n):
            if self.a[i] == u:
                depth = 0
                while i > 0:
                    i = parent(i)
                    depth += 1
                return depth


    def height(self) -> int:
        return int(math.log2(self.n))

    def bf_order(self) -> list:
        if self.n == 0:
            return []
        q = [self.a[0]]
        res = []
        while q:
            node = q.pop(0)
            res.append(node)
            left_child_idx = left(self.a.tolist().index(node))
            if left_child_idx < self.n:
                q.append(self.a[left_child_idx])
            right_child_idx = right(self.a.tolist().index(node))
            if right_child_idx < self.n:
                q.append(self.a[right_child_idx])
        return res


    def in_order(self) -> list:
        # todo
        pass

    def post_order(self) -> list:
        # todo
        pass

    def pre_order(self) -> list:
        # todo
        pass

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        i = self.n - 1
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            self.a[i], self.a[p_idx] = self.a[p_idx], self.a[i]
            i = p_idx
            p_idx = parent(i)

    def _resize(self):
        b = _new_array(max(1, 2 * self.n))
        for i in range(0, self.n):
            b[i] = self.a[i]
        self.a = b

    def _trickle_down_root(self):
        i = 0
        l_idx = left(i)
        r_idx = right(i)
        while i < self.n and l_idx <= self.n and r_idx <= self.n \
                and (self.a[i] > self.a[l_idx] or self.a[i] > self.a[r_idx]):
            if self.a[l_idx] < self.a[r_idx] and self.a[l_idx] < self.a[i]:
                min_idx = l_idx
            elif self.a[r_idx] < self.a[i] and self.a[r_idx] < self.a[l_idx]:
                min_idx = r_idx
            else:
                min_idx = i
            self.a[i], self.a[min_idx] = self.a[min_idx], self.a[i]
            i = min_idx
            l_idx = left(i)
            r_idx = right(i)

    def __str__(self):
        return str(self.a[0:self.n])
