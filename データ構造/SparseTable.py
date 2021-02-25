class SparseTable:
    def __init__(self, array: list):
        n = len(array)
        logn = n.bit_length()
        self.sparse_table = st = [[0] * (n + 1 - (1 << i)) for i in range(logn)]
        st[0] = array
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
        b = self.log[r - l]
        s = self.sparse_table[b]
        return min(s[l], s[r - (1 << b)])
