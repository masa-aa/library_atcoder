def merge(a: list, b: list) -> None:
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


def merge_sort(a: list) -> None:
    n = len(a)
    m = 1
    while m < n:
        m2 = m + m
        for i in range(n // m2):
            merge_array = merge(a[i * m2:i * m2 + m], a[i * m2 + m:(i + 1) * m2])
            k = i * m2
            for j, e in enumerate(merge_array):
                a[k + j] = e
        k = n // m2 * m2
        if n - k > m:
            merge_array = merge(a[k:k + m], a[k + m:])
            for j, e in enumerate(merge_array):
                a[k + j] = e
        m = m2
