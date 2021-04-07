class BinaryIndexedTree:
    def __init__(self, init: int or list):
        if isinstance(init, int):
            self.n = n
            self.tree = [0] * (n + 1)
            self.depth = n.bit_length() - 1
        else:
            self.n = len(init)
            self.tree = [0] * (self.n + 1)
            self.depth = self.n.bit_length() - 1
            for i, e in enumerate(init):
                self.tree[i] += e
                j = i | (i + 1)
                if j < self.n:
                    self.tree[j] += self.tree[i]

    def sum(self, i: int) -> int:
        """ 区間[0,i) の総和を求める """
        s = 0
        i -= 1
        while i >= 0:
            s += self.tree[i]
            i = (i & (i + 1)) - 1
        return s

    def add(self, i: int, x: int) -> None:
        """ i 番目の要素に x を足す """
        while i < self.n:
            self.tree[i] += x
            i |= i + 1

    def get(self, i: int, j: int) -> int:
        """ 部分区間和 [i, j) """
        if i == 0:
            return self.sum(j)
        return self.sum(j) - self.sum(i)

    def lower_bound(self, x: int, equal: bool = False) -> tuple:
        """ (a0+a1+...+ai < x となる最大の i, その時の a0+a1+...+ai )
             a0+a1+...+ai <= x としたい場合は equal = True
             二分探索であるため、ai>=0 を満たす必要がある"""
        sum_ = 0
        pos = -1    # 1-indexed の時は pos = 0
        if not equal:
            for i in range(self.depth, -1, -1):
                k = pos + (1 << i)
                if k < self.n and sum_ + self.tree[k] < x:  # 1-indexed の時は k <= self.n
                    sum_ += self.tree[k]
                    pos += 1 << i
        if equal:
            for i in range(self.depth, -1, -1):
                k = pos + (1 << i)
                if k < self.n and sum_ + self.tree[k] <= x:  # 1-indexed の時は k <= self.n
                    sum_ += self.tree[k]
                    pos += 1 << i
        return pos, sum_

    def __getitem__(self, i: int) -> int:
        return self.get(i, i + 1)

    def __setitem__(self, k: int, x: int) -> None:
        self.add(k, x - self[k])

    def __iter__(self):
        """ [a0, a1, a2, ...] """
        for i in range(self.n):
            yield self.get(i, i + 1)

    def __str__(self):
        text1 = " ".join(["element:            "] + list(map(str, self)))
        text2 = " ".join(["cumsum(1-indexed):  "] + list(str(self.sum(i)) for i in range(1, self.n + 1)))
        return "\n".join((text1, text2))
