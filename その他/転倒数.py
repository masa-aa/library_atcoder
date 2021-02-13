def inversion_number(a: list) -> int:
    """a(0-indexedで座圧済)の転倒数を求める"""
    n = len(a)
    tree = [0] * (n + 1)
    res = n * (n - 1) // 2
    for i in a:
        s = 0
        j = i
        while j >= 0:
            s += tree[j]
            j = (j & (j + 1)) - 1
        res -= s
        while i < n:
            tree[i] += 1
            i |= i + 1
    return res


"""
a(0-indexedで座圧済), bit := Binary Indexed Treeに対して,

res = n * (n - 1) // 2
for i, e in enumerate(a):
    res -= bit.sum(e + 1)
    bit.add(e, 1)

を展開している.
"""
