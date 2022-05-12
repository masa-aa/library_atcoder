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

    def __call__(self, n):
        """nの素因数分解の結果を{素因数:回数}で返す"""
        d = {}
        while n > 1:
            if self.min_factor[n] in d:
                d[self.min_factor[n]] += 1
            else:
                d[self.min_factor[n]] = 1
            n //= self.min_factor[n]
        return d


def lcm_list(a: list, m: int = -1):
    """aのlcmを素数リストで返す（O(nlog(m)), m = max(a) + 1"""
    if m == -1:
        m = max(a) + 1

    fact = factorization(m)
    res = {}
    for i in a:
        for k, x in fact(i).items():
            if k not in res:
                res[k] = x
            else:
                res[k] = max(res[k], x)

    return res
