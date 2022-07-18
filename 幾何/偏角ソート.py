

def ort(p):
    x, y = p
    if y > 0:
        return 1 if x > 0 else 2
    return 3 if x < 0 else 4


def ort2(p):
    """library checker"""
    x, y = p
    if y >= 0:
        return 1 if x >= 0 else 2
    return -1 if x < 0 else 0


def cross(p, q):
    x0, y0 = p
    x1, y1 = q
    return x0 * y1 - x1 * y0


def cmp(p, q):
    if p == q:
        return 1
    o1 = ort(p); o2 = ort(q)
    if o1 == o2:
        return cross(p, q) > 0
    return o1 < o2


def merge_sort(a: list, cmp) -> None:
    """
    cmp(s, t) : s < t を返す．
    """
    n = len(a)
    m = 1
    while m < n:
        m2 = m + m
        for i in range(n // m2):
            im2 = i * m2
            s = a[im2:im2 + m]
            t = a[im2 + m:im2 + m2]
            s_idx = t_idx = 0
            for k in range(im2, im2 + m2):
                if t_idx == m:
                    a[k] = s[s_idx]
                    s_idx += 1
                elif s_idx == m or cmp(t[t_idx], s[s_idx]):  # 比較
                    a[k] = t[t_idx]
                    t_idx += 1
                else:
                    a[k] = s[s_idx]
                    s_idx += 1

        k = n // m2 * m2
        if n - k > m:
            s = a[k:k + m]
            t = a[k + m:]
            t_size = n - k - m
            s_idx = t_idx = 0
            for k in range(k, n):
                if t_idx == t_size:
                    a[k] = s[s_idx]
                    s_idx += 1
                elif s_idx == m or cmp(t[t_idx], s[s_idx]):  # 比較
                    a[k] = t[t_idx]
                    t_idx += 1
                else:
                    a[k] = s[s_idx]
                    s_idx += 1
        m = m2
