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
