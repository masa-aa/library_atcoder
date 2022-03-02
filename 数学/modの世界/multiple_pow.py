from itertools import product
from math import gcd
from random import randrange


class Factorization:
    def __init__(self, n):
        self._n = n
        self.set_primes = self.set_factorization(n)

    def is_prime(self, n):
        """ミラーラビン"""
        v = [2, 7, 61] if n < 4_759_123_141 else \
            [2, 3, 5, 7, 11, 13, 17] if n < 341_550_071_728_321 else \
            [2, 3, 5, 7, 11, 13, 17, 19, 23] if n < 3_825_123_056_546_413_051 else \
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
        if n < 2:
            return False
        if n in v:
            return True
        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1

        for a in v:
            if pow(a, d, n) != 1:
                ok = True
                for r in range(s):
                    if pow(a, d * 1 << r, n) == n - 1:
                        ok = 0
                        break
                if ok:
                    return False
        return True

    def f(self, x, n, c):
        return (x * x + c) % n

    def get_factor(self, n):
        c = randrange(1, n)
        if n % 2 == 0:
            return 2
        if self.is_prime(n):
            return n
        x = randrange(1, n)
        y, d = x, 1

        while d == 1:
            x = self.f(x, n, c)
            y = self.f(self.f(y, n, c), n, c)
            d = gcd(abs(x - y), n)
        if d == n:
            return self.get_factor(n)
        return self.get_factor(d)

    def set_factorization(self, n):
        """素因数分解"""
        if n == 1:
            return []
        arr = []
        while n > 1:
            k = self.get_factor(n)
            arr.append(k)
            while n % k == 0:
                n //= k
        return arr

    def eulers_function(self):
        """オイラー関数"""
        res = 1
        n = self._n
        for i in self.set_primes:
            res *= i - 1
            n //= i
        return res * n


def multiple_pow(a, mod):
    """ a[0]^a[1]^...^a[n] % mod """
    n = len(a) - 1
    phi = [1] * n
    phi[0] = mod
    for i in range(1, n):
        phi[i] = Factorization(phi[i - 1]).eulers_function()
        if phi[i] == 1:
            break
    k = pow(a[-2], a[-1], phi[-1]) + phi[-1]
    print(phi)
    for i in range(n - 2, -1, -1):
        print(k)
        k = pow(a[i], k, phi[i]) + phi[i]
    return k % mod


n, m = map(int, input().split())
a = list(map(int, input().split()))
print(multiple_pow(a, m))
