# 未
class RangeSumQueryAndRangeAddQuery:
    def __init__(self, a):
        if isinstance(a, int):
            self.slope = [0] * (a + 1)
            self.const = [0] * (a + 1)
            self.n = a

    def _add(self, arr: list, k: int, x: int) -> None:
        """arrのk番目にxを足す"""
        while k < self.n:
            arr[k] += x
            k |= k + 1

    def _sum(self, arr: list, k: int) -> int:
        """sum(arr[:k])"""
        s = 0
        k -= 1
        while k >= 0:
            s += arr[k]
            k = (k & (k + 1)) - 1
        return s

    def add(self, l: int, r: int, x: int) -> None:
        self._add(self.slope, l, x)
        self._add(self.slope, r + 1, -x)
        self._add(self.const, l, (1 - l) * x)
        self._add(self.const, r + 1, (r) * x)

    def sum(self, k):
        return self._sum(self.slope, k) * k + self._sum(self.const, k)

    def get(self, l, r):
        if l == 0:
            return self.sum(r)
        return self.sum(r) - self.sum(l - 1)

    def __iter__(self):
        for i in range(self.n):
            yield self.get(i, i + 1)

    def __repr__(self):
        return " ".join(map(str, self))


a = RangeSumQueryAndRangeAddQuery(10)
print(a)
a.add(0, 5, 3)
print(a)
a.add(1, 2, 1)
print(a)
