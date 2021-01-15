"""
前処理:O(NK)
クエリ:O(1)
comb[n][r] = nCr % mod
"""


def table(n=2001, k=2001, mod=1_000_000_007):
    comb = [[0] * k for _ in range(n)]
    for i in range(k):
        comb[i][0] = 1
    for i in range(1, n):
        for j in range(1, k):
            res = comb[i - 1][j] + comb[i - 1][j - 1]
            if res > mod:
                res -= mod
            comb[i][j] = res

    return comb


comb = table()
