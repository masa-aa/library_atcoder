class UnionFind:
    __slots__ = ["N", "root"]

    def __init__(self, N: int) -> None:
        """
        N:要素数
        root:各要素の親要素の番号を格納するリスト.
             ただし, root[x] < 0 ならその頂点が根で-root[x]が木の要素数.
        """
        N += 1
        self.N = N
        self.root = [-1] * N

    def __repr__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

    def find(self, x: int) -> int:
        """頂点xの根を見つける"""
        r = x
        while self.root[r] >= 0:
            r = self.root[r]

        while self.root[x] >= 0:
            self.root[x], x = r, self.root[x]

        return r

    def union(self, x: int, y: int) -> bool:
        """x, yが属する木をunion"""
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False

        elif self.root[y] < self.root[x]:
            x, y = y, x
        self.root[x] += self.root[y]
        self.root[y] = x

        return True

    def same(self, x: int, y: int) -> bool:
        """xとyが同じグループに属するかどうか"""
        return self.find(x) == self.find(y)

    def count(self, x: int) -> int:
        """頂点xが属する木のサイズを返す"""
        return - self.root[self.find(x)]

    def members(self, x: int) -> list:
        """xが属する木の要素を列挙"""
        _root = self.find(x)
        return [i for i in range(self.N) if self.find(i) == _root]

    def roots(self) -> list:
        """森の根を列挙"""
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_count(self) -> int:
        """連結成分の数"""
        res = 0
        for i in self.root:
            if i < 0:
                res += 1
        return res

    def all_group_members(self) -> dict:
        """{ルート要素: [そのグループに含まれる要素のリスト], ...}の辞書を返す"""
        groups = {r: [] for r in self.roots()}
        for i in range(self.N):
            groups[self.find(i)].append(i)
        return groups
