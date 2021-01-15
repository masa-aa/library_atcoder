class WeightedUnionFind:
    __slots__ = ("root", "diff_weight")

    def __init__(self, N):
        """root[v] = vの親, diff_weight[v] = 根からの重み"""
        self.root = [-1] * N
        self.diff_weight = [0] * N

    def find(self, x):
        que = []
        while self.root[x] >= 0:
            que.append(x)
            x = self.root[x]

        for i in reversed(que):
            self.diff_weight[i] += self.diff_weight[self.root[i]]
            self.root[i] = x

        return x

    def weight(self, x):
        self.find(x)
        return self.diff_weight[x]

    def difference(self, x, y):
        """weight(y) - weight(x)"""
        assert self.find(x) == self.find(y)
        return self.diff_weight[y] - self.diff_weight[x]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y, w):
        """weight(y) - weight(x) = w となるように union する"""
        x_root = self.find(x)
        y_root = self.find(y)
        w += self.diff_weight[x]
        w -= self.diff_weight[y]
        x, y = x_root, y_root
        if x == y:
            return
        if self.root[y] < self.root[x]:
            x, y, w = y, x, -w
        self.root[x] += self.root[y]
        self.root[y] = x
        self.diff_weight[y] = w


# verify
# https://onlinejudge.u-aizu.ac.jp/solutions/problem/DSL_1_B/review/4984129/masa_aa/Python3
# https://atcoder.jp/contests/abc087/submissions/18052603
