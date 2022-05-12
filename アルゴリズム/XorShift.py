class Xorshift:
    def __init__(self, init):
        self.x = init

    def __call__(self):
        self.x = self.x ^ (self.x << 7 & 0xFFFFFFFFFFFFFFFF)
        self.x = self.x ^ (self.x >> 9)
        return self.x


class Xorshift32:
    def __init__(self, init):
        self.x = init

    def __call__(self):
        self.x = self.x ^ (self.x << 13 & 0xFFFFFFFF)
        self.x = self.x ^ (self.x >> 17)
        self.x = self.x ^ (self.x << 5 & 0xFFFFFFFF)
        return self.x
