class SparseTable_index:
    """更新がない場合の区間の最小値を高速に求める．<O(nlog(n), O(1))>"""
    __slots__ = ["sparse_table", "log", "array"]

    def __init__(self, array: list):
        """O(nlog(n))"""
        n = len(array)
        logn = n.bit_length()
        self.array = array
        self.sparse_table = st = [[0] * (n + 1 - (1 << i)) for i in range(logn)]
        st[0] = list(range(n))

        for i in range(logn - 1):
            s = st[i]
            t = st[i + 1]
            width = 1 << i
            for j in range(n + 1 - 2 * width):
                first, second = s[j], s[j + width]
                t[j] = first if array[first] < array[second] else second
        self.log = log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i >> 1] + 1

    def prod(self, l: int, r: int) -> int:
        """min(array[l:r])を返す．O(1)"""
        b = self.log[r - l]
        s = self.sparse_table[b]
        first, second = s[l], s[r - (1 << b)]
        return first if self.array[first] < self.array[second] else second
