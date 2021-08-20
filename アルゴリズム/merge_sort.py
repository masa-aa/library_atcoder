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
            # merge_array = merge(a[i * m2:i * m2 + m], a[i * m2 + m:(i + 1) * m2])
            s = a[i * m2:i * m2 + m]
            t = a[i * m2 + m:(i + 1) * m2]
            k = i * m2
            s_idx = t_idx = 0
            for k in range(i * m2, (i + 1) * m2):
                if t_idx == m:
                    a[k] = s[s_idx]
                    s_idx += 1
                elif t_idx == m or t[t_idx] < s[s_idx]:
                    a[k] = t[t_idx]
                    t_idx += 1
                else:
                    a[k] = s[s_idx]
                    s_idx += 1

        k = n // m2 * m2
        if n - k > m:
            # merge_array = merge(a[k:k + m], a[k + m:])
            s = a[k:k + m]
            t = a[k + m:]
            t_size = n - k - m
            s_idx = t_idx = 0
            for k in range(k, n):
                if t_idx == t_size:
                    a[k] = s[s_idx]
                    s_idx += 1
                elif t_idx == m or t[t_idx] < s[s_idx]:
                    a[k] = t[t_idx]
                    t_idx += 1
                else:
                    a[k] = s[s_idx]
                    s_idx += 1
        m = m2
