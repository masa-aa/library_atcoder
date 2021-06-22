def show(graph):
    """隣接リストを可視化するツール"""
    import networkx as nx
    import matplotlib.pyplot as plt
    g = nx.Graph()
    g.add_nodes_from(range(1, len(graph) + 1))
    for i in range(len(graph)):
        for j in graph[i]:
            if i < j:
                g.add_edge(i + 1, j + 1)
    nx.draw_networkx(g)
    plt.show()
