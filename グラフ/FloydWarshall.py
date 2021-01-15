def FloydWarshall(d, INF=2_000_000_000_000_000):
    """破壊的処理"""
    n = len(d)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] == INF or d[k][j] == INF:
                    continue
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    # if any(d[i][i] < 0 for i in range(n)): # 負の閉路があるなら0を返す.
    #     return 0
    return d


INF = 2_000_000_000_000_000
n, m = map(int, input().split())
d = [[INF] * n for i in range(n)]
# 入力
for i in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    d[a][b] = c
    d[b][a] = c  # 無向グラフ
for i in range(n):
    d[i][i] = 0

dd = FloydWarshall(d)
print(d)
