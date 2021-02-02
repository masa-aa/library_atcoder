def bellman_ford(start: "始点", V: "頂点数", es: "隣接リスト", INF=10000000000):
    """負の閉路が存在すればFalseを返す"""
    # INF = 10**10 毎回チェックしよう
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
            break
    else:
        # 負の閉路が存在
        return False
    return d


n, m = map(int, input().split())
es = [[] for _ in range(n)]  # es[i] = (頂点iの(隣接する頂点,コスト)の組)

# 入力
for i in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    es[a].append((b, c))
    es[b].append((a, c))  # 無向グラフ
