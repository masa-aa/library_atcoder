import sys
sys.setrecursionlimit(10000000)


class BipartiteMatching:
    """集合Aから集合Bに辺が貼られているような二部グラフ"""

    def __init__(self, n: int, m: int):
        """n : A のサイズ, m : B のサイズ"""
        self.size = n + m
        self._n = n
        self._g = [[] for _ in range(n)]
        self.matchA = [-1] * n
        self.matchB = [-1] * m

    def add_edge(self, u: int, v: int) -> None:
        """辺を追加. u はAの頂点，vはBの頂点 """
        self._g[u].append(v)

    def _dfs(self, v):
        self.used[v] = True
        for u in self._g[v]:
            w = self.matchB[u]
            if w < 0 or not self.used[w] and self._dfs(w):
                self.matchA[v] = u
                self.matchB[u] = v
                return True
        return False

    def bipartite_matching(self) -> int:
        """マッチするペアの個数を返す"""
        res = 0
        for v in range(self._n):
            if self.matchA[v] < 0:
                self.used = [0] * self._n
                if self._dfs(v):
                    res += 1
        return res

    def match(self) -> list:
        """マッチするペアのリストを返す"""
        self.bipartite_matching()
        self.matches = []
        for u, v in enumerate(self.matchA):
            if v >= 0:
                self.matches.append((u, v))
        return self.matches

    def show(self):
        """グラフを可視化する．誰かが作ってくれる"""
        self.bipartite_matching()


# https://yukicoder.me/submissions/624295
# https://onlinejudge.u-aizu.ac.jp/solutions/problem/GRL_7_A/review/5493145/masa_aa/Python3
