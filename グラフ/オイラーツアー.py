from array import array


def euler_tour(G: "隣接リスト", root: "根"):
    """euler tourしてleft idとright idと深さのlistを返す"""
    n = len(G)
    tour = [0] * (2 * n - 1)
    depth_list = []
    left_id = [-1] * n
    right_id = [-1] * n
    v = root
    it = [0] * n
    parents = [-1] * n
    visit_id = 0
    depth = 0
    while v != -1:
        if left_id[v] == -1:
            left_id[v] = visit_id
            if len(depth_list) <= depth:
                depth_list.append([array("i")])
            depth_list[depth].append(visit_id)

        right_id[v] = visit_id
        tour[visit_id] = v
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
    return left_id, right_id, depth_list
