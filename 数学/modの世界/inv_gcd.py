def inv_gcd(a, b):
    """
        (gcd(a, b), x) を返す．
        ただし x は, ax = gcd(a, b), 0 <= x < b/gcd(a, b) を満たす.
    """
    # note gcd(a, b) = 1 なら mod 逆元
    a %= b
    if a == 0:
        return b, 0
    s, t = b, a
    m0, m1 = 0, 1
    while t:
        u = s // t
        s -= t * u; m0 -= m1 * u
        s, t = t, s; m0, m1 = m1, m0

    if m0 < 0:
        m0 += b // s

    return s, m0
