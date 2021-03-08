from array import array
from collections import deque


def cycle(G: "隣接リスト") -> list:
    """グラフのサイクル検出をする．"""
    # memo 有向グラフの時はparentsを消すとパフォーマンスが向上する．
    n = len(G)
    seen = [0] * n
    finished = [0] * n
    parents = [-1] * n
    for root in range(n):
        if seen[root]:
            continue
        hist = deque()
        que = deque()
        que.append(~root); que.append(root)
        while que:
            v = que.pop()
            if v >= 0:
                seen[v] = 1
                hist.append(v)
                for e in G[v]:
                    if parents[v] == e:
                        continue
                    if finished[e]:
                        continue
                    if seen[e] and not finished[e]:
                        while hist:
                            if hist[0] == e:
                                break
                            hist.popleft()
                        return list(hist)
                    que.append(~e); que.append(e)
                    parents[e] = v
            else:
                hist.pop()
                finished[~v] = 1

    return []


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
es = [array("i") for _ in range(n)]
for i in range(m):
    start, end = map(int, input().split())
    # start -= 1; end -= 1
    es[start].append(end)
    # es[end].append(start)
