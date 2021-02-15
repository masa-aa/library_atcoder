from collections import deque


def diameter_of_tree(es: "隣接リスト", weight=False, start=0):
    """木の直径を返す"""
    bfs = shortest_path_bfs_weight if weight else shortest_path_bfs
    d = bfs(es, start)
    start = d.index(max(d))
    d = bfs(es, start)
    return max(d)


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


def shortest_path_bfs_weight(es: "隣接リスト", start: "始点"):
    INF = 1_000_000_000_000_000_000
    V = len(es)
    d = [INF] * V  # 頂点startからの最短距離
    que = deque()
    que.append(start)
    d[start] = 0
    while que:
        v = que.popleft()
        for e, de in es[v]:
            if d[e] == INF:
                d[e] = d[v] + de
                que.append(e)
    return d


import sys
input = sys.stdin.readline

n = int(input())
es = [[] for _ in range(n)]
# 入力
for _ in range(n - 1):
    start, end, distance = map(int, input().split())
    start -= 1; end -= 1
    es[start].append((end, distance))
    es[end].append((start, distance))  # 無向グラフ

print(diameter_of_tree(es, weight=1))
