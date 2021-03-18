def isqrt(n: int) -> int:
    """a = floor(sqrt(n))) (とr = n - a*a)を返す."""
    a = 0; r = 0
    for s in reversed(range(0, n.bit_length(), 2)):
        t = n >> s & 3
        r = r << 2 | t
        c = a << 2 | 1
        b = r >= c
        if b:
            r -= c
        a = a << 1 | b
    return a
    # return a, r
