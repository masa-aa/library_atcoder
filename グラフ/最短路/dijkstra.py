from heapq import heappush, heapify, heappop


def dijkstra(es: "隣接リスト", start: "始点", INF=2000000000000000):
    # INF = 2 * 10**15 (> 10**6 * 10**9)
    V = len(es)
    d = [INF] * V  # 頂点sからの最短距離
    que = [(0, start)]  # (距離, 頂点)
    d[start] = 0
    while que:
        dv, v = heappop(que)
        if d[v] < dv:
            continue
        for e, de in es[v]:
            if d[e] > d[v] + de:
                d[e] = d[v] + de
                heappush(que, (d[e], e))
    return d


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
es = [[] for _ in range(n)]  # es[i] = (頂点iの(隣接する頂点,コスト)の組)
# 入力
for _ in range(m):
    start, end, distance = map(int, input().split())
    start -= 1; end -= 1
    es[start].append((end, distance))
    es[end].append((start, distance))  # 無向グラフ
