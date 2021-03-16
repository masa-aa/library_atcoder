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


def crt(r: list, m: list) -> tuple:
    """数列r, mに対して連立合同式 x ≡ ri (mod mi)(0<=i<n) の解の計算"""
    # assert len(r) == len(m)
    r0, m0 = 0, 1
    for r1, m1 in zip(r, m):
        # assert m1 >= 1
        r1 %= m1
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0

        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return 0, 0
            continue
        _gcd, im = inv_gcd(m0, m1)
        if (r1 - r0) % _gcd:
            return 0, 0

        u1 = m0 * m1 // _gcd
        r0 += (r1 - r0) // _gcd * m0 * im % u1
        m0 = u1

    return r0, m0
