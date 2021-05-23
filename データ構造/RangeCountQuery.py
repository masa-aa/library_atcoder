from bisect import bisect_left
from array import array


class RangeCountQueryCompressed:
    """N = len(arr) としたとき 0<=a[i]<N"""

    def __init__(self, arr):
        self.size = max(arr) + 1
        self.depth = [array("i") for _ in range(self.size)]
        for i, e in enumerate(arr):
            self.depth[e].append(i)

    def count(self, l, r, x):
        """l <= k < r におけるa[k]=xの個数"""
        if x >= self.size:
            return 0
        a = self.depth[x]
        s = bisect_left(a, l)
        t = bisect_left(a, r, s)
        return t - s


from bisect import bisect_left
from array import array
from collections import defaultdict


class RangeCountQuery:
    def __init__(self, arr):
        self.depth = defaultdict(list)
        for i, e in enumerate(arr):
            self.depth[e].append(i)

    def count(self, l, r, x):
        """l <= k < r におけるa[k]=xの個数"""
        a = self.depth[x]
        s = bisect_left(a, l)
        t = bisect_left(a, r, s)
        return t - s

