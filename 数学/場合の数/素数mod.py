# テーブル作るやつ 前処理:O(n), comb(n, k):O(1)
mod = 10**9 + 7  # 998244353 # 変える


def table():
    k = 2 * 10 ** 5 + 5  # 変える
    fac = [1] * k
    finv = [1] * k
    inv = [0] * k
    inv[1] = 1
    for i in range(2, k):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    return fac, finv


fac, finv = table()


def comb(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % mod) % mod


def perm(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * finv[n - k] % mod
