# テーブル作るやつ 前処理:O(n), comb(n, k):O(1)

def table():
    fac = [1] * table_size
    finv = [1] * table_size
    inv = [0] * table_size
    inv[1] = 1
    for i in range(2, table_size):
        fac[i] = fac[i - 1] * i % mod
        div = mod // i
        inv[i] = mod - inv[mod - i * div] * div % mod
        finv[i] = finv[i - 1] * inv[i] % mod
    return fac, finv


def comb(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * finv[k] % mod * finv[n - k] % mod


def perm(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * finv[n - k] % mod


mod = 1_000_000_007  # 998244353 # 変える
table_size = 10**6 + 10  # 変える
fac, finv = table()
