from array import array


def RangeSetQuery(arr: list, query: list):
    "aはcompressed, aの[l, r)における種類数を求める．"
    n = len(arr)
    pi = [-1] * (n + 1)  # 各数について最後に出てきた場所
    ps = [array("i") for _ in range(n)]

    for i in range(n):
        l = pi[arr[i]]
        # 2つ目以降
        if l != -1:
            ps[l].append(i)
        # 1つ目
        pi[arr[i]] = i

    qs = [[] for _ in range(n)]
    for i, (l, r) in enumerate(query):
        qs[l].append((r - 1, i))

    d = [0] * (n + 1)
    res = [0] * len(query)

    # x座標を後ろから見ていく
    for x in range(n - 1, -1, -1):
        for y in ps[x]:
            while y <= n:
                d[y] += 1
                y += y & (-y)

        for r, i in qs[x]:
            # r以下のものがans
            s = 0
            idx = r
            while idx > 0:
                s += d[idx]
                idx -= idx & (-idx)
            res[i] = r - x + 1 - s

    return res
