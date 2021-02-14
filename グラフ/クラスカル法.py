def krascal(n: "頂点数", D: "隣接リスト"):
    """D[i] = (x, y, (x, y)間のcost), 最小全域木のコストを返す"""
    uf = UnionFind(n)
    D.sort(key=lambda x: x[2])
    cost = 0
    for x, y, c in D:
        if not uf.same(x, y):
            uf.union(x, y)
            cost += c
    return cost


class UnionFind:
    __slots__ = ["root"]

    def __init__(self, N):
        self.root = [-1] * N

    def find(self, x):
        while self.root[x] >= 0:
            x = self.root[x]
        return x

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        elif self.root[y] < self.root[x]:
            x, y = y, x
        self.root[x] += self.root[y]
        self.root[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


# if __name__ == '__main__':
#     n = 7
#     d = [[0, 1, 3], [1, 2, 2], [2, 3, 60], [3, 4, 3], [4, 5, 7], [5, 6, 9], [2, 6, 100], [5, 6, 100]]

#     print(krascal(n, d))
#     # >>> 84
