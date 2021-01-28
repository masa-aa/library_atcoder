class RangeAddQuery:
    """区間add更新, 一点取得"""
    __slots__ = ["n", "tree"]

    def __init__(self, n_or_list):
        """
        :param n_or_list: 要素数か初期化するlist
        """
        if isinstance(n_or_list, int):
            self.n = n_or_list
            self.tree = [0] * (n_or_list + 1)
        else:
            self.n = len(n_or_list)
            self.tree = [0] * (self.n + 1)
            add = self.add
            for i, e in enumerate(n_or_list):
                add(i, i + 1, e)

    def add(self, s, t, x):
        """ [s, t)にxを足す. """
        n = self.n
        tree = self.tree
        while s < n:
            tree[s] += x
            s |= s + 1
        while t < n:
            tree[t] -= x
            t |= t + 1

    def get(self, i):
        """ i番目(0-indexed)を返す. """
        res = 0
        tree = self.tree
        while i >= 0:
            res += tree[i]
            i = (i & (i + 1)) - 1
        return res

    def __repr__(self):
        return ">> " + " ".join(map(str, self))

    def __getitem__(self, i):
        """ i番目(0-indexed)を返す. """
        return self.get(i)

    def __iter__(self):
        for i in range(self.n):
            yield self.get(i)

    def __list__(self):
        return list(self)
