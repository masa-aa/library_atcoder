class SparseTable_index:
    def __init__(self, array: list):
        n = len(array)
        logn = n.bit_length()
        self.array = array
        self.sparse_table = st = [[0] * (n + 1 - (1 << i)) for i in range(logn)]
        s = st[0]
        for i in range(n):
            s[i] = i
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
        b = self.log[r - l]
        s = self.sparse_table[b]
        first, second = s[l], s[r - (1 << b)]
        return first if self.array[first] < self.array[second] else second
