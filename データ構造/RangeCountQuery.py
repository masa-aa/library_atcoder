from bisect import bisect_left
from array import array


class RangeCountQueryCompressed:
    def __init__(self, arr):
        self.size = max(arr) + 1
        self.depth = [array("i") for _ in range(self.size)]
        for i, e in enumerate(arr):
            self.depth[e].append(i)

    def count(self, l, r, x):
        if x >= self.size:
            return 0
        s = bisect_left(self.depth[x], l)
        t = bisect_left(self.depth[x], r, s)
        return t - s


from bisect import bisect_left
from array import array
from collections import defaultdict


class RangeCountQuery:
    def __init__(self, arr):
        self.size = max(arr) + 1
        self.depth = defaultdict(list)
        for i, e in enumerate(arr):
            self.depth[e].append(i)

    def count(self, l, r, x):
        s = bisect_left(self.depth[x], l)
        t = bisect_left(self.depth[x], r, s)
        return t - s
