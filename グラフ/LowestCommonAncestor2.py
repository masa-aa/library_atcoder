class LowestCommonAncestor:
    """ <O(Nlog(N)), O(1)> """
    __slots__ = ["n", "tour", "depth_list", "id", "sparse_table", "log"]

    def __init__(self, G: "隣接リスト", root: "根"):
        self.n = len(G)
        self.tour = [0] * (2 * self.n - 1)
        self.depth_list = [0] * (2 * self.n - 1)
        self.id = [-1] * self.n
        self.dfs(G, root)
        self._rmq_init(self.depth_list)

    def _rmq_init(self, array):
        n = len(array)
        logn = n.bit_length()
        self.sparse_table = st = [[0] * (n + 1 - (1 << i)) for i in range(logn)]
        st[0] = list(range(n))

        for i in range(logn - 1):
            s = st[i]
            t = st[i + 1]
            width = 1 << i
            for j in range(n + 1 - 2 * width):
                first, second = s[j], s[j + width]
                t[j] = first if array[first] < array[second] else second
        self.log = log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i >> 1] + 1

    def _rmq_query(self, l: int, r: int) -> int:
        """min(array[l:r])を返す．O(1)"""
        b = self.log[r - l]
        s = self.sparse_table[b]
        first, second = s[l], s[r - (1 << b)]
        return first if self.depth_list[first] < self.depth_list[second] else second

    def dfs(self, G, root):
        """ 非再帰で深さ優先探索を行う """
        id = self.id
        tour = self.tour
        depth_list = self.depth_list
        v = root
        it = [0] * self.n
        parents = [-1] * self.n
        visit_id = 0
        depth = 0
        while v != -1:
            if id[v] == -1:
                id[v] = visit_id
            tour[visit_id] = v
            depth_list[visit_id] = depth
            visit_id += 1
            g = G[v]
            if it[v] == len(g):
                v = parents[v]
                depth -= 1
                continue
            if g[it[v]] == parents[v]:
                it[v] += 1
                if it[v] == len(g):
                    v = parents[v]
                    depth -= 1
                    continue
                else:
                    child = g[it[v]]
                    parents[child] = v
                    it[v] += 1
                    v = child
                    depth += 1
            else:
                child = g[it[v]]
                parents[child] = v
                it[v] += 1
                v = child
                depth += 1

    def lca(self, u: int, v: int) -> int:
        """ u と v の最小共通祖先を返す """
        l, r = self.id[u], self.id[v]
        if r < l:
            l, r = r, l
        q = self._rmq_query(l, r + 1)
        return self.tour[q]

    def dist(self, u: int, v: int) -> int:
        """ u と v の距離を返す """
        lca = self.lca(u, v)
        depth_u = self.depth_list[self.id[u]]
        depth_v = self.depth_list[self.id[v]]
        depth_lca = self.depth_list[self.id[lca]]
        return depth_u + depth_v - 2 * depth_lca
