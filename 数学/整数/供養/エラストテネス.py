from math import ceil, sqrt


def PopCnt(bits):
    bits = (bits & 0x5555555555555555) + ((bits >> 1) & 0x5555555555555555)
    bits = (bits & 0x3333333333333333) + ((bits >> 2) & 0x3333333333333333)
    bits = (bits & 0x0f0f0f0f0f0f0f0f) + ((bits >> 4) & 0x0f0f0f0f0f0f0f0f)
    return (bits * 0x0101010101010101) >> (64 - 8)


def BitToIndex(b):
    if b == 1 << 0:
        return 0
    elif b == 1 << 1:
        return 1
    elif b == 1 << 2:
        return 2
    elif b == 1 << 3:
        return 3
    elif b == 1 << 4:
        return 4
    elif b == 1 << 5:
        return 5
    elif b == 1 << 6:
        return 6
    elif b == 1 << 7:
        return 7
    return -1


class Eratosthenes:
    def __init__(self, x):
        kMod30 = [1, 7, 11, 13, 17, 19, 23, 29]
        C1 = [6, 4, 2, 4, 2, 4, 6, 2]
        C0 = [
            [0, 0, 0, 0, 0, 0, 0, 1], [1, 1, 1, 0, 1, 1, 1, 1],
            [2, 2, 0, 2, 0, 2, 2, 1], [3, 1, 1, 2, 1, 1, 3, 1],
            [3, 3, 1, 2, 1, 3, 3, 1], [4, 2, 2, 2, 2, 2, 4, 1],
            [5, 3, 1, 4, 1, 3, 5, 1], [6, 4, 2, 4, 2, 4, 6, 1]
        ]
        kMask = [
            [0xfe, 0xfd, 0xfb, 0xf7, 0xef, 0xdf, 0xbf, 0x7f],
            [0xfd, 0xdf, 0xef, 0xfe, 0x7f, 0xf7, 0xfb, 0xbf],
            [0xfb, 0xef, 0xfe, 0xbf, 0xfd, 0x7f, 0xf7, 0xdf],
            [0xf7, 0xfe, 0xbf, 0xdf, 0xfb, 0xfd, 0x7f, 0xef],
            [0xef, 0x7f, 0xfd, 0xfb, 0xdf, 0xbf, 0xfe, 0xf7],
            [0xdf, 0xf7, 0x7f, 0xfd, 0xbf, 0xfe, 0xef, 0xfb],
            [0xbf, 0xfb, 0xf7, 0x7f, 0xfe, 0xef, 0xdf, 0xfd],
            [0x7f, 0xbf, 0xdf, 0xef, 0xf7, 0xfb, 0xfd, 0xfe],
        ]
        if x > 10000000000:
            return
        size = x // 30 + (x % 30 != 0)
        self.flags_ = [0xff] * size
        r = x % 30
        if r:
            if r <= 1: self.flags_[size - 1] = 0x0
            elif r <= 7: self.flags_[size - 1] = 0x1
            elif r <= 11: self.flags_[size - 1] = 0x3
            elif r <= 13: self.flags_[size - 1] = 0x7
            elif r <= 17: self.flags_[size - 1] = 0xf
            elif r <= 19: self.flags_[size - 1] = 0x1f
            elif r <= 23: self.flags_[size - 1] = 0x3f
            elif r <= 29: self.flags_[size - 1] = 0x7f
        self.flags_[0] = 0xfe
        sqrt_x = ceil(sqrt(x) + 0.1)
        sqrt_xi = sqrt_x // 30 + 1
        for i in range(sqrt_xi):
            flags = self.flags_[i]
            while flags:
                lsb = flags & (-flags)
                ibit = BitToIndex(lsb)
                m = kMod30[ibit]
                pm = 30 * i + 2 * m
                j = i * pm + m * m // 30
                k = ibit
                while j < len(self.flags_):
                    self.flags_[j] &= kMask[ibit][k]
                    j += i * C1[k] + C0[ibit][k]
                    k = (k + 1) & 7
                flags &= flags - 1

    def count(self):
        if self.flags_:
            ret = 3
            for f in self.flags_:
                ret += PopCnt(f)
            return ret
        return -1


def sieve(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0] = False

    for i in range(2, n + 1):
        if is_prime[i - 1]:
            j = 2 * i
            while j <= n:
                is_prime[j - 1] = False
                j += i
    table = [i for i in range(1, n + 1) if is_prime[i - 1]]
    return table


for i in range(1, 101):
    e = Eratosthenes(i)
    print(i, len(sieve(i)), e.count())
