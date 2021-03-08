import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
from array import array
from collections import deque


def dfs(v, p):
    global pos
    seen[v] = 1
    hist.append(v)
    for nv in es[v]:
        if nv == p:
            continue
        if finished[nv]:
            continue
        if seen[nv] and not finished[nv]:
            pos = nv
            return

        dfs(nv, v)

        if pos != -1:
            return
    hist.pop()
    finished[v] = 1


n, m = map(int, input().split())
es = [array("i") for _ in range(n)]
for i in range(m):
    start, end = map(int, input().split())
    start -= 1; end -= 1
    es[start].append(end)

seen = [0] * n
finished = [0] * n
hist = deque()

pos = -1
for i in range(n):
    if not seen[i]:
        dfs(i, -1)
    if pos != -1:
        print(1)
        exit()

print(0)
