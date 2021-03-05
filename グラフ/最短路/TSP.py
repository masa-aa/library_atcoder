def TSP(dist: "距離行列"):
    # "*"の部分を変える
    n = len(dist)
    INF = 10_000_000_000
    dp = [[INF] * n for _ in range(1 << n)]
    "*"
    # for i in range(n):  # 任意始点
    #     dp[1 << i][i] = 0
    dp[0][0] = 0
    for u in range(n):
        for v in range(n):
            dp[1 << v][v] = min(dp[1 << v][v], dp[0][u] + dist[u][v])
    "*"
    for S in range(1, 1 << n):
        for u in range(n):
            if not S >> u & 1:
                continue
            for v in range(n):
                if S >> v & 1:
                    continue
                dp[S + (1 << v)][v] = min(dp[S + (1 << v)][v], dp[S][u] + dist[u][v])
    return dp[-1]
