def merge(a: list, b: list) -> list:
    """sort列 a, b の sorted(a + b)と等価なものをO(N + M)でする"""
    p = len(a)
    q = len(b)
    s = [0] * (p + q)
    i = j = 0
    for k in range(p + q):
        if i == p:
            s[k] = b[j]
            j += 1
        elif j == q or a[i] < b[j]:
            s[k] = a[i]
            i += 1
        else:
            s[k] = b[j]
            j += 1
    return s
