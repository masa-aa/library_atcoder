from heapq import heappush, heapify, heappop


def dijkstra(start: "始点", V: "頂点数", es: "隣接リスト", INF=10000000000):
    # INF = 10**10 毎回チェックしよう
    prev = [-1] * n  # 経路復元
    d = [INF] * n  # 頂点sからの最短距離
    que = [start]
    d[start] = 0
    while que:
        dv, v = divmod(heappop(que), INF)
        if d[v] < dv:
            continue
        for e, de in es[v]:
            if d[e] > d[v] + de:
                d[e] = d[v] + de
                heappush(que, d[e] * INF + e)
                prev[e] = v
    return d, prev


def get_path(t, prev):
    path = []
    while t != -1:
        path.append(t)
        t = prev[t]
    path.reverse()
    return path


n, m = map(int, input().split())
es = [[] for _ in range(n)]  # es[i] = (頂点iの(隣接する頂点,コスト)の組)
# 入力
for i in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    es[a].append((b, c))
    es[b].append((a, c))  # 無向グラフ
