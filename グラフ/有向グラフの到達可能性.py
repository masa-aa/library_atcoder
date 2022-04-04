from collections import deque


class StronglyConnectedComponents:
    # naniwazuくんのやついじった

    def __init__(self, n):
        self.size = n
        self.edges = []
        self._group_num = -1

    def _csr(self):
        self.start = [0] * (self.size + 1)
        self.elist = [0] * len(self.edges)
        for e_start, _ in self.edges:
            self.start[e_start + 1] += 1
        for i in range(1, self.size + 1):
            self.start[i] += self.start[i - 1]
        counter = self.start[:]
        for e_start, e_end in self.edges:
            self.elist[counter[e_start]] = e_end
            counter[e_start] += 1

    def add_edge(self, u, v):
        self.edges.append((u, v))

    def _scc_id_construct(self):
        self._csr()
        n = self.size
        now_ord = group_num = 0
        visited = []
        low = [0] * n
        order = [-1] * n
        ids = [0] * n
        parent = [-1] * n
        stack = []
        for i in range(n):
            if order[i] == -1:
                stack.append(i)
                stack.append(i)
                while stack:
                    v = stack.pop()
                    if order[v] == -1:
                        low[v] = order[v] = now_ord
                        now_ord += 1
                        visited.append(v)
                        for i in range(self.start[v], self.start[v + 1]):
                            to = self.elist[i]
                            if order[to] == -1:
                                stack.append(to)
                                stack.append(to)
                                parent[to] = v
                            else:
                                low[v] = min(low[v], order[to])
                    else:
                        if low[v] == order[v]:
                            while True:
                                u = visited.pop()
                                order[u] = n
                                ids[u] = group_num
                                if u == v:
                                    break
                            group_num += 1
                        if parent[v] != -1:
                            low[parent[v]] = min(low[parent[v]], low[v])
        for i, x in enumerate(ids):
            ids[i] = group_num - 1 - x

        self._group_num = group_num
        self._ids = ids

    def strongly_connected_components(self):

        if self._group_num == -1:
            self._scc_id_construct()

        group_num = self._group_num
        ids = self._ids
        groups = [[] for _ in range(group_num)]
        for i, x in enumerate(ids):
            groups[x].append(i)

        return groups

    def construct_reduction_graph(self):
        """縮約したグラフを返す"""

        if self._group_num == -1:
            self._scc_id_construct()

        group_num = self._group_num
        ids = self._ids
        graph = [[] for _ in range(group_num)]
        for s, t in self.edges:
            graph[ids[s]].append(ids[t])

        # 多重辺, 自己ループ削除
        reduction_graph = [[] for _ in range(group_num)]
        last = [-1] * group_num
        for u, edges in enumerate(graph):
            for v in edges:
                if last[v] != u and u != v:
                    last[v] = u
                    reduction_graph[u].append(v)

        return reduction_graph


def offline_directed_graph_reachability(input_graph, queries):
    """queries[i] = (u, v), u -> v に到達可能かを答える"""
    n = len(input_graph)
    scc = StronglyConnectedComponents(n)
    for i in range(n):
        for j in input_graph[i]:
            scc.add_edge(i, j)
    graph = scc.construct_reduction_graph()
    ids = scc._ids

    n = len(graph)
    q = len(queries)
    ans = [0] * q
    buff_size = 1000

    for l in range(0, q, buff_size):
        r = min(q, l + buff_size)
        dp = [0] * n

        for k in range(l, r):
            dp[ids[queries[k][0]]] |= 1 << (k - l)

        for idx in range(n):
            for to in graph[idx]:
                dp[to] |= dp[idx]

        for k in range(l, r):
            ans[k] = dp[ids[queries[k][1]]] >> (k - l) & 1

    return ans
