"""n種類の数a_iがそれぞれm_i個ずつあります。
これらの中からいくつか選び、その総和を
ちょうどKとすることができるか判定しなさい。
制約
1≤n≤100
1≤a_i,m_i≤10^5
1≤K≤10^5
​
!!TLE!!
"""
n=int(input())
a=list(map(int, input().split()))
m=list(map(int, input().split()))
K=int(input())
dp=[[False for i in range(K+1)] for j in range(n+1)]
dp[0][0]=True
for i in range(n):
    for j in range(K+1):
        for k in range(m[i]+1):
            if k*a[i]>j:
                break
            else:
                dp[i+1][j]|=dp[i][j-k*a[i]]###
if dp[k][n]==True:
    print("Yes")
else:
    print("No")
#print(dp)
