"""
s以下の3を含む数はいくつあるか.

1<=s<=10**100
"""
s = input()
n = [int(i) for i in s]
l = len(s)
dp = [[[0, 0], [0, 0]] for i in range(l + 1)]
dp[0][0][0] = 1
for i in range(l):
    for smaller in range(2):
        for j in range(2):
            for x in range(10 if smaller else n[i] + 1):
                dp[i + 1][smaller or x < n[i]][j or x == 3] += dp[i][smaller][j]
print(dp[l][0][1] + dp[l][1][1])
