class factorization:
    def __init__(self, N=1_000_010):
        """min_factor[i] = iの最小の素因数"""
        self.min_factor = list(range(N))
        for i in range(2, N):
            if i * i > N:
                break
            for j in range(i * i, N, i):
                if self.min_factor[j] == j:
                    # 小さくできるなら小さくするmin_factor[j] != j => i < j
                    self.min_factor[j] = i

    def fact(self, n):
        """nの素因数分解の結果を{素因数:回数}で返す"""
        d = {}
        while n > 1:
            if self.min_factor[n] in d:
                d[self.min_factor[n]] += 1
            else:
                d[self.min_factor[n]] = 1
            n //= self.min_factor[n]
        return d

    def count_divisors(self, n):
        res = 1
        for v in self.fact(n).values():
            res *= v + 1
        return res

    def sum_divisors(self, n):
        res = 1
        for r, Len in self.fact(n).items():
            res *= (r ** (Len + 1) - 1) // (r - 1)
        return res

    def Eulers_function(self, n):
        res = 1
        for i in self.fact(n):
            res *= (i - 1)
            n //= i
        return res * n
