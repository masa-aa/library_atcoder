# (始点, 終点, cost)で持つと高速化につながる.

def bellman_ford(es: "隣接リスト", start: "始点", INF=1_000_000_000_000_000_000):
    """負の閉路が存在すればFalseを返す"""
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
            break
    else:
        # 負の閉路が存在
        return False
    return d


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
es = [[] for _ in range(n)]
for i in range(m):
    start, end, weight = map(int, input().split())
    start -= 1; end -= 1
    es[start].append((end, weight))
    es[end].append((start, weight))
