from collections import deque


def topological_sort(V, es):
    _es = [[] for _ in range(V)]
    deg = [0] * V
    for i in range(V):
        for e in es[i]:
            _es[e].append(i)
            deg[i] += 1
    d = deque()
    for i, deg_i in enumerate(deg):
        if deg_i == 0:
            d.append(i)
    order = []
    while d:
        v = d.popleft()
        order.append(v)
        for i in _es[v]:
            deg[i] -= 1
            if deg[i] == 0:
                d.append(i)
    order.reverse()
    return order


n, m = map(int, input().split())
es = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    es[a].append(b)
