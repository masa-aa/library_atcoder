# 実装例
# https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_b
from heapq import heappush, heapify, heappop


def dijkstra(a: "コスト", sx, sy: "始点", INF=2000000000000000):
    d = [[INF] * c for _ in range(r)]   # 頂点sからの最短距離
    que = [(0, sx, sy)]  # (距離, 頂点)
    d[sx][sy] = 0
    while que:
        dv, vx, vy = heappop(que)
        if d[vx][vy] < dv:
            continue

        for dx, dy in ([(-1, 0), (1, 0), (0, 1), (0, -1), (1, 1), (-1, 1)] if vx & 1 else [(-1, 0), (1, 0), (0, 1), (0, -1), (1, -1), (-1, -1)]):
            x = vx + dx
            y = vy + dy
            if 0 <= x < r and 0 <= y < c and d[x][y] > d[vx][vy] + a[x][y]:
                d[x][y] = d[vx][vy] + a[x][y]
                heappush(que, (d[x][y], x, y))

    return d


import sys
def input(): return sys.stdin.readline().rstrip()  # 文字列


r, c = map(int, input().split())

a = []
for i in range(r):
    t = input()
    k = t.find("s")
    if k >= 0:
        sx, sy = i, k
        t = t.replace("s", "0")
    k = t.find("t")
    if k >= 0:
        tx, ty = i, k
        t = t.replace("t", "0")
    a.append(list(map(int, t)))

print(dijkstra(a, sx, sy)[tx][ty])
