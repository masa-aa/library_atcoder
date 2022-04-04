from collections import deque


def topological_sort(es):
    V = len(es)
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


def offline_dag_reachability(graph, queries):
    """queries[i] = (u, v), u -> v に到達可能かを答える"""
    n = len(graph)
    q = len(queries)
    order = topological_sort(graph)
    ans = [0] * q
    buff_size = 62

    for l in range(0, q, buff_size):
        r = min(q, l + buff_size)
        dp = [0] * n

        for k in range(l, r):
            dp[queries[k][0]] |= 1 << (k - l)

        for idx in order:
            for to in graph[idx]:
                dp[to] |= dp[idx]

        for k in range(l, r):
            ans[k] = dp[queries[k][1]] >> (k - l) & 1

    return ans
