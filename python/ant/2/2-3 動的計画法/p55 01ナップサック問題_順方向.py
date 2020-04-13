"""
重さと価値がそれぞれw_i,v_iであるようなn個の品物がある.
これらの品物の中から, 重さの総和がWを超えないように選んだ時の,
価値の総和の最大値を求めよ.
1<=n<=100, 1<=w_i,v_i<=100, 1<=W<=10000
"""
#-------------------------------------------------------------------------------
n = int(input())
w=[0]*n
v=[0]*n
for i in range(n):
    x,y = map(int, input().split())
    w[i] = x
    v[i] = y
W = int(input())
dp = [[0 for i in range(W+1)] for j in range(n+1)]
for i in range(n):
    for j in range(W+1):
        if j < w[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - w[i]] + v[i])
#print(dp)
print(dp[n][W])
