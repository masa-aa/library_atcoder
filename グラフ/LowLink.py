class LowLink:
    def __init__(self, G, root=0):
        self.n = n = len(G)
        self.order = [-1] * n
        self.lowlink = [0] * n
        self.dfs(G, root)

    def dfs(self, G, root):
        """ 非再帰で深さ優先探索を行う """
        order = self.order
        lowlink = self.lowlink
        use = [0] * self.n
        v = root
        it = [0] * self.n
        parents = [-1] * self.n
        num = 0
        while v != -1:
            print(v)
            use[v] = 1
            order[v] = lowlink[v] = num
            num += 1
            g = G[v]
            while it[v] < len(g) and use[g[it[v]]]:
                it[v] += 1
            if it[v] == len(g):
                v = parents[v]
            else:
                child = g[it[v]]
                parents[child] = v
                it[v] += 1
                v = child


es = [[1, 4], [0, 2, 3], [1], [1], [0, 5], [4]]
LowLink(es)
