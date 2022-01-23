mod = 998_244_353


def fast_pow(a: int, k: int):
    """
        a^k % mod
        modをglobalに取って高速化
    """
    a %= mod
    res = 1 % mod
    while k:
        if k & 1:
            res = a * res % mod
        a = a * a % mod
        k >>= 1

    return res
