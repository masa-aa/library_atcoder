from collections import deque


def shortest_path_bfs(es: "隣接リスト", start: "始点"):
    INF = 1_000_000_000
    V = len(es)
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

    return d


import sys
input = sys.stdin.readline
from array import array

n, m = map(int, input().split())
es = [array("i") for _ in range(n)]
for i in range(m):
    start, end = map(int, input().split())
    start -= 1; end -= 1
    es[start].append(end)
    es[end].append(start)  # 無向グラフ

s = int(input()) - 1
k = int(input()) + 1
dist = [[0] * k for _ in range(k)]

t = array("i", map(lambda x: int(x) - 1, input().split()))
t.insert(0, s)

for i, e in enumerate(t):
    d = shortest_path_bfs(es, e)
    dist[i] = [d[i] for i in t]


