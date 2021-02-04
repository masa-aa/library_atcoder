class SegmentTree:
    def __init__(self, init, op, e):
        """
        init : int か list
        op : min, +, *, xor, gcd など
        e : 単位元(min:inf, 和:0, 積:1, xor:0, gcd:0)
        """
        self.op = op
        self.e = e
        if isinstance(init, int):
            self.size = 1 << (init - 1).bit_length()
            self.seg = [e] * (2 * self.size)
        else:
            n = len(init)
            self.size = 1 << (n - 1).bit_length()
            self.seg = [e] * (2 * self.size)
            seg = self.seg
            for i, e in enumerate(init):
                seg[i + self.size] = e
            for i in range(self.size - 1, 0, -1):
                seg[i] = op(seg[2 * i], seg[2 * i + 1])

    def __getitem__(self, k):
        return self.seg[k + self.size]

    def __setitem__(self, k, x):
        return self.set(k, x)

    def set(self, k, x):
        """k番目の要素の値をxに変更"""
        k += self.size
        seg = self.seg
        seg[k] = x
        while k > 1:
            k >>= 1
            seg[k] = self.op(seg[2 * k], seg[2 * k + 1])

    def prod(self, l, r):
        """op(a[l], ..., a[r - 1])"""
        l += self.size; r += self.size
        s = self.e
        # 区間を列挙しながら最小値などをを求める
        while l < r:
            if r & 1:
                r -= 1
                s = self.op(s, self.seg[r])
            if l & 1:
                s = self.op(s, self.seg[l])
                l += 1
            l >>= 1
            r >>= 1
        return s

    def all_prod(self):
        return self.seg[1]

    def update(self, k, x):
        """k番目の要素の値をop(seg[k], x)に更新"""
        self.set(k, self.op(self[k], x))

    def debug(self):
        n = len(self.seg).bit_length()
        res = []
        k = 1
        for _ in range(1, n + 1):
            res.append(" ".join(map(str, self.seg[k:2 * k])))
            k *= 2
        k //= 2
        print("-" * k)
        print("\n".join(res))
        print("-" * k)

    def __repr__(self):
        return " ".join(map(str, self.seg[self.size:]))
