class LowLink:
    """単純連結なグラフに対して橋，関節点の列挙をO(N + M)で行う．"""
    """多重辺，自己ループは未対応であることに注意"""

    def __init__(self, G, root=0):
        self.n = n = len(G)
        self.root = root
        self.order = [-1] * n
        self.lowlink = [0] * n
        self.parents = [-1] * n
        self.G = G
        self._dfs(root)

    def _dfs(self, root):
        """ 非再帰で深さ優先探索を行う """
        G = self.G
        order = self.order
        lowlink = self.lowlink
        use = [0] * self.n
        v = root
        it = [0] * self.n
        parents = self.parents
        num = 0
        while True:
            use[v] = 1
            if order[v] == -1:
                order[v] = lowlink[v] = num
                num += 1
            g = G[v]
            while it[v] < len(g) and use[g[it[v]]]:
                if parents[v] != g[it[v]]:
                    lowlink[v] = min(order[g[it[v]]], lowlink[v])
                it[v] += 1
            if it[v] == len(g):
                if v == root:
                    break
                lowlink[parents[v]] = min(lowlink[parents[v]], lowlink[v])
                v = parents[v]
            else:
                child = g[it[v]]
                parents[child] = v
                it[v] += 1
                v = child

    def bridge(self):
        """橋のリストを返す．"""
        G = self.G
        order = self.order
        lowlink = self.lowlink
        res = []
        for v, g in enumerate(G):
            for u in g:
                if order[v] < lowlink[u]:
                    res.append((v, u))
        return res

    def articulation_point(self):
        """関節点のリスト(ソート済)を返す．"""
        G = self.G
        root = self.root
        order = self.order
        lowlink = self.lowlink
        parents = self.parents
        res = []
        for v, g in enumerate(G):
            if v == root:
                childs = 0
                for u in g:
                    if parents[u] == root:
                        if childs:
                            res.append(v)
                            break
                        childs += 1
                continue
            for u in g:
                if parents[u] == v and order[v] <= lowlink[u]:
                    res.append(v)
                    break
        return res


# 関節点
# https://onlinejudge.u-aizu.ac.jp/solutions/problem/GRL_3_A/review/5243835/masa_aa/Python3

# 橋
# https://onlinejudge.u-aizu.ac.jp/solutions/problem/GRL_3_B/review/5231887/masa_aa/Python3
