def count_dictionary_order(a: list, mod=1_000_000_007) -> int:
    """0 or 1-indexedの順列が与えられてそれが辞書順何番目か(1-indexed)を返す"""
    n = len(a)
    tree = [0] * (n + 1)
    res = 1
    fac = 1
    for i, e in enumerate(a[::-1], 1):
        s = 0
        k = e - 1
        while k >= 0:
            s += tree[k]
            k = (k & (k + 1)) - 1
        res += fac * s
        while e < n:
            tree[e] += 1
            e |= e + 1
        fac *= i
        fac %= mod
    return res % mod


"""
bit := Binary Indexed Treeに対して,

res = 1
fac = 1
for i, e in enumerate(a[::-1], 1):
    res += fac * bit.sum(e)
    bit.add(e, 1)
    fac *= i
    fac %= mod

を展開している.
"""
