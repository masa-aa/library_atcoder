def merge(a, b):
    """sort列 a, b の sorted(a + b)と等価なものをO(N + M)でする"""
    n, m = len(a), len(b)
    c = [0] * (n + m)
    j, k = 0, 0
    for i in range(n + m):
        if k == m:
            for i in range(i, n + m):
                c[i] = a[j]
                j += 1
            break
        elif j == n:
            for i in range(i, n + m):
                c[i] = b[k]
                k += 1
            break
        elif a[j] <= b[k]:
            c[i] = a[j]
            j += 1
        else:
            c[i] = b[k]
            k += 1
    return c
