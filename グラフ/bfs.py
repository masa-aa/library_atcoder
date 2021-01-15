from collections import deque


def shortest_path_bfs(start: "始点", V: "頂点数", es: "隣接リスト", INF=10000000000):
    # INF = 10**10 毎回チェックしよう
    prev = [-1] * n  # 経路復元
    d = [INF] * n  # 頂点sからの最短距離
    deq = deque()
    deq.append(start)
    d[start] = 0
    while deq:
        v = deq.popleft()
        for e in es[v]:
            if d[e] == INF:
                d[e] = d[v] + 1
                deq.append(e)
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
es = [[] for _ in range(n)]
# 入力
for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    es[a].append(b)
    es[b].append(a)  # 無向グラフ
