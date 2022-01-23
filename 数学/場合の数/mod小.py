"""mod:素数, 構築O(mod^2), クエリO(log(k))"""


def table() -> list:
    t = [[0] * mod for _ in range(mod)]
    for i in range(mod):
        t[i][0] = 1
    for i in range(1, mod):
        for j in range(1, mod):
            res = t[i - 1][j] + t[i - 1][j - 1]
            if res > mod:
                res -= mod
            t[i][j] = res

    return t


def comb(n: int, k: int) -> int:
    """modが小さい場合のnCk"""
    if n < k or n < 0 or k < 0:
        return 0
    if n - k < k:
        k = n - k
    ans = 1
    while k:
        p = n // mod
        q = k // mod
        s = n - p * mod
        t = k - q * mod
        ans *= cmb[s][t]
        ans %= mod
        n = p
        k = q
    return ans


mod = 3  # 変える
cmb = table()
