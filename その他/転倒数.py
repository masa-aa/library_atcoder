def inversion_number(a: list) -> int:
    """a(0 or -indexedで座圧済)の転倒数を求める"""
    n = len(a)
    tree = [0] * (n + 1)
    res = n * (n - 1) // 2
    for i in a:
        s = 0
        j = i - 1
        while j >= 0:
            s += tree[j]
            j = (j & (j + 1)) - 1
        res -= s
        while i < n:
            tree[i] += 1
            i |= i + 1
    print(tree)
    return res


"""
a(0 or 1-indexedで座圧済), bit := Binary Indexed Treeに対して,

res = 0
for i, e in enumerate(a):
    res += i - bit.sum(e)
    bit.add(e, 1)

を展開している.
"""
