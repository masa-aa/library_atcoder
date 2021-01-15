def ternary_search(l, r):
    """[l, r)においてf(x)が極小となるkを求める. 極大は不等号逆"""
    l -= 1
    while r - l > 2:
        ll = (l + l + r) // 3
        rr = (l + r + r) // 3
        if f(ll) < f(rr):
            r = rr
        else:
            l = ll
    return (l + r) // 2


def f(k):
    return a[k]


a = [100, 99, 98, 3, 21, 11, 2]
print(ternary_search(0, len(a)))
