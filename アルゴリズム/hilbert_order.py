# どこまでライブラリ化すればいいかわからんからとりあえず張る

def merge_sort(a: list, key) -> None:
    od = list(map(key, a))
    n = len(a)
    m = 1
    while m < n:
        m2 = m + m
        for i in range(n // m2):
            im2 = i * m2
            s = a[im2:im2 + m]
            t = a[im2 + m:im2 + m2]
            s2 = od[im2:im2 + m]
            t2 = od[im2 + m:im2 + m2]
            s_idx = t_idx = 0
            for k in range(im2, im2 + m2):
                if t_idx == m:
                    a[k] = s[s_idx]
                    od[k] = s2[s_idx]
                    s_idx += 1
                elif s_idx == m or t2[t_idx] < s2[s_idx]:  # 比較
                    a[k] = t[t_idx]
                    od[k] = t2[t_idx]
                    t_idx += 1
                else:
                    a[k] = s[s_idx]
                    od[k] = s2[s_idx]
                    s_idx += 1

        k = n // m2 * m2
        if n - k > m:
            s = a[k:k + m]
            t = a[k + m:]
            s2 = od[k:k + m]
            t2 = od[k + m:]
            t_size = n - k - m
            s_idx = t_idx = 0
            for k in range(k, n):
                if t_idx == t_size:
                    a[k] = s[s_idx]
                    od[k] = s2[s_idx]
                    s_idx += 1
                elif s_idx == m or t2[t_idx] < s2[s_idx]:  # 比較
                    a[k] = t[t_idx]
                    od[k] = t2[t_idx]
                    t_idx += 1
                else:
                    a[k] = s[s_idx]
                    od[k] = s2[s_idx]
                    s_idx += 1
        m = m2


def hilbert_order(x, y):
    LOG = 20
    MAXN = 1 << LOG
    d = 0
    s = 1 << (LOG - 1)

    while s:
        rx = x & s > 0
        ry = y & s > 0
        s >>= 1
        d = (d << 2) | ((rx * 3) ^ ry)

        if ry:
            continue

        if rx:
            x = MAXN - x
            y = MAXN - y

        x, y = y, x

    return d


import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
q = int(input())
query = [0] * q
for i in range(q):
    l, r = map(int, input().split())
    query[i] = (l - 1, r - 1, i)

merge_sort(query, lambda x: hilbert_order(x[0], x[1]))

cnt = [0] * (n + 1)
ans = [0] * q
curl, curr = 0, -1
res = 0

for l, r, i in query:
    while l < curl:
        curl -= 1
        k = a[curl]
        if cnt[k]:
            cnt[k] = 0
            res += 1
        else:
            cnt[k] = 1

    while l > curl:
        k = a[curl]
        if cnt[k]:
            cnt[k] = 0
        else:
            cnt[k] = 1
            res -= 1
        curl += 1

    while r < curr:
        k = a[curr]
        if cnt[k]:
            cnt[k] = 0
        else:
            cnt[k] = 1
            res -= 1
        curr -= 1

    while r > curr:
        curr += 1
        k = a[curr]
        if cnt[k]:
            cnt[k] = 0
            res += 1
        else:
            cnt[k] = 1

    ans[i] = res

print(*ans)
