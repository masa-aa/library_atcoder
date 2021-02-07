# issue dfsが再帰
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline


class LowestCommonAncestor:
    def __init__(self, G: "隣接リスト", root: "根"):
        self.n = len(G)
        self.tour = [0] * (2 * self.n - 1)
        self.depth_list = [0] * (2 * self.n - 1)
        self.id = [0] * self.n
        self.visit_id = 0
        self._dfs(G, root, -1, 0)
        self._rmq_init(self.depth_list)

    def _rmq_init(self, arr):
        n = self.mod = len(arr)
        self.seg_len = 1 << (n - 1).bit_length()
        self.seg = [self.n * n] * (2 * self.seg_len)
        seg = self.seg
        for i, e in enumerate(arr):
            seg[self.seg_len + i] = n * e + i
        for i in range(self.seg_len - 1, 0, -1):
            seg[i] = min(seg[2 * i], seg[2 * i + 1])

    def _rmq_query(self, l, r):
        """最小値となるindexを返す"""
        l += self.seg_len; r += self.seg_len
        res = self.n * self.mod
        seg = self.seg
        while l < r:
            if r & 1:
                r -= 1
                res = min(res, seg[r])
            if l & 1:
                res = min(res, seg[l])
                l += 1
            l >>= 1; r >>= 1
        return res % self.mod

    def _dfs(self, G, vertex, parent, depth):
        self.id[vertex] = self.visit_id
        self.tour[self.visit_id] = vertex
        self.depth_list[self.visit_id] = depth
        self.visit_id += 1
        for element in G[vertex]:
            if element != parent:
                self._dfs(G, element, vertex, depth + 1)
                self.tour[self.visit_id] = vertex
                self.depth_list[self.visit_id] = depth
                self.visit_id += 1

    def lca(self, u: int, v: int) -> int:
        """ u と v の最小共通祖先を返す."""
        l, r = self.id[u], self.id[v]
        if r < l:
            l, r = r, l
        q = self._rmq_query(l, r + 1)
        return self.tour[q]

    def dist(self, u: int, v: int) -> int:
        """ u と v の距離を返す"""
        lca = self.lca(u, v)
        depth_u = self.depth_list[self.id[u]]
        depth_v = self.depth_list[self.id[v]]
        depth_lca = self.depth_list[self.id[lca]]
        return depth_u + depth_v - 2 * depth_lca
