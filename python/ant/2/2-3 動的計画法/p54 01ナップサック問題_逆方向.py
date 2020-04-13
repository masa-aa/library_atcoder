"""
重さと価値がそれぞれw_i,v_iであるようなn個の品物がある.
これらの品物の中から, 重さの総和がWを超えないように選んだ時の,
価値の総和の最大値を求めよ.
1<=n<=100, 1<=w_i,v_i<=100, 1<=W<=10000
"""
#-------------------------------------------------------------------------------
n = int(input())
wv = [list(map(int, input().split())) for i in range(n)]
W = int(input())
dp = [[0 for i in range(W+1)] for j in range(n+1)]
for i in range(n - 1, -1, -1):
    for j in range(W+1):
        if j < wv[i][0]:
            dp[i][j] = dp[i + 1][j]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - wv[i][0]] + wv[i][1])
#print(dp)
print(dp[0][W])
