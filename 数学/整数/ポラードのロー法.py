from collections import Counter
from itertools import product
from math import gcd
from random import randrange


class Factorization:
    def __init__(self, n):
        self._n = n
        self.primes = self.factorization(n)

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

    def factorization(self, n):
        """素因数分解"""
        if n == 1:
            return []
        arr = []
        while n > 1:
            k = self.get_factor(n)
            while n % k == 0:
                n //= k
                arr.append(k)
        return arr

    def divisors(self):
        """約数列挙"""
        if not self.primes:
            return [1]
        c = Counter(self.primes)
        mul_list = []
        for i in c:
            tmp = [1] * (c[i] + 1)
            for j in range(c[i]):
                tmp[j + 1] = tmp[j] * i
            mul_list.append(tmp)

        res = []
        for v in product(*mul_list):
            k = 1
            for x in v:
                k *= x
            res.append(k)
        return res

    def count_divisors(self):
        """約数の個数"""
        res = 1
        for i in Counter(self.primes).values():
            res *= i + 1
        return res

    def sum_divisors(self):
        """約数の総和"""
        res = 1
        c = Counter(self.primes)
        for i in c:
            res *= (i ** (c[i] + 1) - 1) // (i - 1)
        return res

    def eulers_function(self):
        """オイラー関数"""
        res = 1
        n = self._n
        for i in set(self.primes):
            res *= i - 1
            n //= i
        return res * n

    def __iter__(self):
        for i in self.primes:
            yield i

    def __repr__(self):
        return f"factorization({self._n}) : {self.primes}"

    # def cpp_divisors(self):
    # """Pythonだと遅い"""
    # if not self.primes:
    #     return [1]
    # c = Counter(self.primes)
    # mul_list = []
    # loops = []
    # for i in c:
    #     tmp = [1] * (c[i] + 1)
    #     for j in range(c[i]):
    #         tmp[j + 1] = tmp[j] * i
    #     mul_list.append(tmp)
    #     loops.append(c[i] + 1)

    # res = [1]
    # n = len(loops)
    # d = [0] * n
    # loop_count = 1
    # for i in loops:
    #     loop_count *= i

    # for _ in range(loop_count - 1):
    #     d[0] += 1
    #     i = 0
    #     while i < n and d[i] == loops[i]:
    #         d[i] = 0
    #         i += 1
    #         d[i] += 1
    #     k = 1
    #     for i, x in enumerate(d):
    #         k *= mul_list[i][x]
    #     res.append(k)
    # return res


# verify
# https://judge.yosupo.jp/problem/factorize
