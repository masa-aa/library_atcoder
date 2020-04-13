"""
長さnの数列a0,a1,a2...an-1があります。この数列の部分増加列のうち、最長のものの長さを求めなさい。
ただし、増加部分列とは、全てのi<jでai>ajを持たす部分列を言います。

制約
1<=n<=1000
0<=ai<=1000000
"""

n=5
a=[4,2,3,1,5]
dp=[0 for i in range(n)]

def solve():
    res=0
    for i in range(n):
        dp[i]=1
        for j in range(i): #あるaiにおいて、その左にある数を見ている
            if a[j]<a[i]:　#その左のものがaiより小さい場合に
                dp[i]=max(dp[i],dp[j]+1) #dp[i]=1 か 小さい数までに使った数+1 のマックスを取る
        res=max(res,dp[i])
        print(i,dp)
    print(dp)
    print(res)


solve()
