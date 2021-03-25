class SparseTable:
    """更新がない場合の区間の最小値を高速に求める．<O(nlog(n), O(1))>"""
    # max, min, gcd等 冪等半群
    __slots__ = ["sparse_table", "log"]

    def __init__(self, array: list):
        """O(nlog(n))"""
        n = len(array)
        logn = n.bit_length()
        self.sparse_table = st = [[0] * (n + 1 - (1 << i)) for i in range(logn)]
        st[0] = array.copy()
        for i in range(logn - 1):
            s = st[i]
            t = st[i + 1]
            width = 1 << i
            for j in range(n + 1 - 2 * width):
                t[j] = min(s[j], s[j + width])

        # logの前計算
        self.log = log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i >> 1] + 1

    def prod(self, l: int, r: int) -> int:
        """min(array[l:r])を返す．O(1)"""
        # l < r 以外の入力は認められない．
        # if l >= r:
        #     return 1 << 60
        b = self.log[r - l]
        s = self.sparse_table[b]
        return min(s[l], s[r - (1 << b)])

    def __repr__(self):
        return "\n".join("width={}:".format(1 << v) + str(e) for v, e in enumerate(self.sparse_table))
