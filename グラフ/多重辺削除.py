def delete_multiple_edges(edge_list: list) -> list:
    """
        多重辺を削除する
        edge_list : 隣接リスト
    """
    n = len(edge_list)
    res = [[] for _ in range(n)]
    last = [-1] * n
    for u, edges in enumerate(edge_list):
        for v in edges:
            if last[v] != u:
                last[v] = u
                res[u].append(v)
    return res
