def inv(a, m):
    """z/mz のaの逆元を返す.(Euclidの互除法)"""
    b, u, v = m, 1, 0
    while b:
        t = a // b
        a -= t * b
        a, b = b, a
        u -= t * v
        u, v = v, u
    u %= m
    if u < 0:
        u += m
    return u


"""
 modが素数の時, z/mz のaの逆元を返す.(Fermatの小定理)
"""
# pow(a, mod-2, mod)
