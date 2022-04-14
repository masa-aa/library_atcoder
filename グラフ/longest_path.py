from collections import deque


def longest_path(es):
    """DAGの各頂点で終わるlongetst pathの長さ"""
    V = len(es)
    deg = [0] * V
    dp = [0] * V  # dp[i] = 頂点iで終わる最長のpathの長さ
    for i in range(V):
        for e in es[i]:
            deg[e] += 1
    d = deque()
    for i, deg_i in enumerate(deg):
        if deg_i == 0:
            d.append(i)

    while d:
        v = d.popleft()
        for i in es[v]:
            deg[i] -= 1
            if deg[i] == 0:
                d.append(i)
                dp[i] = dp[v] + 1
    return dp


import sys
input = sys.stdin.readline
from array import array

n, m = map(int, input().split())
es = [array("i") for _ in range(n)]
for i in range(m):
    start, end = map(int, input().split())
    start -= 1; end -= 1
    es[start].append(end)
