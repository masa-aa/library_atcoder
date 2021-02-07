def dijkstra(dist: "隣接行列", start: "始点", INF=2000000000000000):
    """ O(V^2) """
    # INF = 2 * 10**15 (> 10**6 * 10**9)
    V = len(dist)
    d = [INF] * V  # 頂点sからの最短距離
    used = [1] * V  # 1なら使われていない
    d[start] = 0
    while True:
        v = -1
        for u in range(V):  # 最小な頂点を探す.
            if used[u] and (v == -1 or d[u] < d[v]):
                v = u
        if v == -1:
            break
        used[v] = 0
        _dist = dist[v]
        for u in range(V):
            d[u] = min(d[u], d[v] + _dist[u])
    return d


import sys
input = sys.stdin.readline


INF = 2000000000000000
n, m = map(int, input().split())
dist = [[INF] * n for _ in range(n)]
for i in range(m):
    start, end, distance = map(int, input().split())
    start -= 1; end -= 1
    dist[start][end] = distance
    dist[end][start] = distance  # 無向グラフ
