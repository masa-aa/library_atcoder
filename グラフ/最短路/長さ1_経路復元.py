from collections import deque


def shortest_path_bfs(es: "隣接リスト", start: "始点"):
    V = len(es)
    INF = 1_000_000_000
    prev = [-1] * V  # 経路復元
    d = [INF] * V  # 頂点startからの最短距離
    que = deque()
    que.append(start)
    d[start] = 0
    while que:
        v = que.popleft()
        for e in es[v]:
            if d[e] == INF:
                d[e] = d[v] + 1
                que.append(e)
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
