# 未完成
# 多重辺　未対応
class LowLink:
    def __init__(self, G, root=0):
        self.n = n = len(G)
        self.root = root
        self.order = [-1] * n
        self.lowlink = [0] * n
        self.parents = [-1] * n
        self.G = G
        self.dfs(root)

    def dfs(self, root):
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
        G = self.G
        order = self.order
        lowlink = self.lowlink
        res = []
        for u, g in enumerate(G):
            for v in g:
                if order[u] < lowlink[v]:
                    res.append((u, v))
        return res

    def articulation_point(self):
        G = self.G
        root = self.root
        order = self.order
        lowlink = self.lowlink
        parents = self.parents
        res = set()
        for u, g in enumerate(G):
            if u == root:
                if parents.count(u) >= 2:
                    res.add(u)
                continue
            for v in g:
                if parents[u] == v:
                    continue
                if order[u] <= lowlink[v]:
                    res.add(u)
        return res


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
es = [[] for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    es[x].append(y)
    es[y].append(x)

res = LowLink(es).articulation_point()
res = sorted(res)
if res:
    print(*res, sep="\n")
print(LowLink(es).bridge())
