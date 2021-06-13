def perm(n, k, mod=1_000_000_007):
    """nPk % mod"""
    if n < k or n < 0 or k < 0:
        return 0
    res = 1
    for i in range(n - k + 1, n + 1):
        res *= i
        res %= mod
    return res
