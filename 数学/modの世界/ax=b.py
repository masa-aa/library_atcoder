from math import gcd


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
    return u


def linear_equation(a, b, mod):
    """ax = b (mod) となるような x を返す．存在しないとき-1を返す"""
    g = gcd(a, mod)
    if b % g:
        return - 1
    a //= g; b //= g; mod //= g
    return b * inv(a, mod) % mod
