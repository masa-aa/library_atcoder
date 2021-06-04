class RhoGraph:
    def __init__(self, x: int, f: "map"):
        """
        写像 f:[l, r] -> [l, r]
        min(f), max(f)がわかるならnum_setとしてlistを使うといい．
        """
        stk = []
        num_set = set()
        while x not in num_set:
            stk.append(x)
            num_set.add(x)
            x = f(x)
        self.loop_start = stk.index(x)
        self.loop_size = len(stk) - self.loop_start
        self.graph = stk

    def query(self, k: int) -> int:
        """
        xにfをk回作用させたもの，f^(k) (x) を返す．
        """
        if k <= self.loop_start:
            return self.graph[k]
        return self.graph[self.loop_start + (k - self.loop_start) % self.loop_size]

    def show(self):
        import networkx as nx
        import matplotlib.pyplot as plt

        g = nx.DiGraph()
        g.add_nodes_from(self.graph)
        for i in range(len(self.graph) - 1):
            g.add_edge(self.graph[i], self.graph[i + 1], weight=i + 1)
        g.add_edge(self.graph[-1], self.graph[self.loop_start], weight=len(self.graph))
        edge_labels = {(i, j): w['weight'] for i, j, w in g.edges(data=True)}
        edge_labels
        pos = nx.spring_layout(g, k=0.7)
        nx.draw_networkx(g, pos, node_color=["c"] * (self.loop_start) + ["r"] * (self.loop_size), with_labels=True, alpha=0.8)
        # nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)
        print("tail :", " -> ".join(map(str, self.tail())))
        print("head :", " -> ".join(map(str, self.head() + self.head()[:1])), "-> ...")

        plt.show()

    def tail(self) -> list:
        """ループに入るまでのlist"""
        return self.graph[:self.loop_start]

    def head(self) -> list:
        """ループの中の要素のlist"""
        return self.graph[self.loop_start:]
