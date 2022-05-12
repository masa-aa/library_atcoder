# setの要素をrand()で変換してxorするだけ

class Xorshift:
    def __init__(self, init):
        self.x = init

    def __call__(self):
        self.x = self.x ^ (self.x << 7 & 0xFFFFFFFFFFFFFFFF)
        self.x = self.x ^ (self.x >> 9)
        return self.x


class Xorshift32:
    # 速い
    def __init__(self, init):
        self.x = init

    def __call__(self):
        self.x = self.x ^ (self.x << 13 & 0xFFFFFFFF)
        self.x = self.x ^ (self.x >> 17)
        self.x = self.x ^ (self.x << 5 & 0xFFFFFFFF)
        return self.x


class ZobristHash:
    def __init__(self):
        self.rand = Xorshift(88172645463325252)
        self.r = {}

    def __call__(self, s: set):
        res = 0
        for i in s:
            if i not in self.r:
                self.r[i] = self.rand()
            res ^= self.r[i]
        return res
