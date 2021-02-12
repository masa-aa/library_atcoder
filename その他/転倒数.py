def inversion_number(a: list) -> int:
    """a(0-indexedで座圧済)の転倒数を求める"""
    n = len(a)
    tree = [0] * (n + 1)
    res = 0
    for i, e in enumerate(a):
        s = 0
        j = e - 1
        while j >= 0:
            s += tree[j]
            j = (j & (j + 1)) - 1
        res += i - s
        while e < n:
            tree[e] += 1
            e |= e + 1
    return res


"""
a(0-indexedで座圧済), bit := Binary Indexed Treeに対して,

res = 0
for i, e in enumerate(a):
    res += i - bit.sum(e)
    bit.add(e, 1)

を展開している.
"""
