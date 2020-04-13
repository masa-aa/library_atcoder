"""
重さと価値がそれぞれw_i,v_iであるようなn個の品物がある.
これらの品物の中から, 重さの総和がWを超えないように選んだ時の,
価値の総和の最大値を求めよ.
1<=n<=100, 1<=w_i<=10^7, 1<=v_i<=100, 1<=limit_w<=10^9
"""
#-------------------------------------------------------------------------------

#入力
INF = 2000000000
"""
メモ : Pythonでは無限大を表す float('inf') があるが, 処理がかなり重たいので
       代わりにsum(v)より真に大きい 2*10^9 を INFとする.
       (https://atcoder.jp/contests/dp/tasks/dp_e において,PyPyを使用して,
        前者だと1060ms, 後者だと570msで2倍近く差が出ている.)
"""
n = int(input())
w = [0]*n
v = [0]*n
for i in range(n):
    w[i], v[i] = map(int, input().split())
limit_w = int(input())
sum_v = sum(v)
dp = [[INF for i in range(sum_v + 1)] for j in range(n + 1)]
# dp[i][j]には重さが入る.
# dp[i][j]=(i番目までの品物から価値がちょうどｊになるための重さの最小値)

# ここからメイン
dp[0][0] = 0
for i in range(n):
    for j in range(sum_v + 1):
        if j < v[i]:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])

# n個まで使って,重さがlimit_wを超えないで価値が最大のものを求める.
max_value = 0
for i in range(sum_v + 1):
    if dp[n][i] <= limit_w:
        max_value = i
print(max_value)
"""
従来の方法だとO(n*limit_w)でlimit_w<=10^9なので間に合わないが,
今回は, 計算量はO(n*sum(v))<=O(n^2*max(v))で間に合う.
"""
