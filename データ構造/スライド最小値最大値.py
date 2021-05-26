from collections import deque


class SlidingMinimumElement:
    def __init__(self, a: list):
        self.left = 0
        self.right = 0
        self.a = a
        self.que = deque()

    def min(self, l: int, r: int):
        """ min(a[l:r]), l,rはクエリに関して単調増加"""
        a = self.a
        que = self.que
        for i in range(self.right, r):
            t = a[i]
            while que and a[que[-1]] > t:
                que.pop()
            que.append(i)
        for i in range(self.left, l):
            if que[0] <= i:  # queには要素があるはず
                que.popleft()
        self.left = l
        self.right = r
        return a[que[0]] if que else 1000000000000000000


# ---------------------------------------------------
from collections import deque


class SlidingMaximumElement:
    def __init__(self, a: list):
        self.left = 0
        self.right = 0
        self.a = a
        self.que = deque()

    def max(self, l: int, r: int):
        """ max(a[l:r]), l,rはクエリに関して単調増加"""
        a = self.a
        que = self.que
        for i in range(self.right, r):
            t = a[i]
            while que and a[que[-1]] < t:
                que.pop()
            que.append(i)
        for i in range(self.left, l):
            if que[0] <= i:  # queには要素があるはず
                que.popleft()
        self.left = l
        self.right = r
        return a[que[0]] if que else -1000000000000000000
