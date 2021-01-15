def num_divisors_table(N):
    """N以下の約数の個数 (sieveっぽい) O(nlog(n))"""
    table = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            table[j] += 1
    return table

# http://sucrose.hatenablog.com/entry/2014/10/10/235805

# 類題
# https://atcoder.jp/contests/abc172/tasks/abc172_d
