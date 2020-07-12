"""
長さnの数列a0,a1,a2...an-1があります。この数列の部分増加列のうち、最長のものの長さを求めなさい。
ただし、増加部分列とは、全てのi<jでai<ajを持たす部分列を言います。

制約
1<=n<=1000
0<=ai<=1000000
"""

from bisect import bisect_left
n=int(input())
a=list(map(int,input().split()))

INF=10**18
dp=[INF for i in range(n)]
for i in range(n):
    lower_index=bisect_left(dp,a[i])
    # print(lower_index)
    dp[lower_index]=a[i]
print(bisect_left(dp,INF))
#print(dp)
