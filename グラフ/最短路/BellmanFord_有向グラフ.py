def bellman_ford(es: "隣接リスト", start: "始点", end: "終点", INF=1_000_000_000_000_000_000):
    """
       始点と終点を与えて終点が負閉路に含まれるか判定する．
       負閉路に含まれるなら-INFを返す．
       そうでないなら始点からの最短経路長を返す．
    """
    V = len(es)
    d = [INF] * V  # 各頂点への最小コスト
    d[start] = 0  # 自身への距離は0
    for _ in range(V):
        update = False  # 更新が行われたか
        for v, e in enumerate(es):
            for t, cost in e:
                if d[v] != INF and d[v] + cost < d[t]:
                    d[t] = d[v] + cost
                    update = True
        if not update:
            return d[end]
    # d[end]が負閉路に含まれるか検出
    res = d[end]
    for _ in range(V):
        for v, e in enumerate(es):
            for t, cost in e:
                if d[v] != INF and d[v] + cost < d[t]:
                    d[t] = -INF
        if d[end] == -INF:
            return -INF
    return res
