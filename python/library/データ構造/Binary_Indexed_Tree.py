class BIT:
    def __init__(self, n):
        #A1 ... AnのBIT(1-indexed)
        self.BIT = [0] * (n + 1)
        self.n = n

    #A1 ~ Aiまでの和 O(logN)
    def query(self, idx):
        res_sum = 0
        while idx > 0:
            res_sum += self.BIT[idx]
            idx -= idx & (-idx)
        return res_sum

    #Ai += x O(logN)
    def add(self, idx, x):
        while idx <= self.n:
            self.BIT[idx] += x
            idx += idx&(-idx)
        return

d = BIT(10)
d.add(2, 2)
d.add(1, 3)
print(d.query(2))
