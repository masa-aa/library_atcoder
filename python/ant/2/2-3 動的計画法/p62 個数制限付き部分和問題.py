"""n種類の数a_iがそれぞれm_i個ずつあります。
これらの中からいくつか選び、その総和を
ちょうどKとすることができるか判定しなさい。
制約
1≤n≤100
1≤a_i,m_i≤10^5
1≤K≤10^5
"""
n=int(input())
a=list(map(int, input().split()))
m=list(map(int, input().split()))
K=int(input())
dp=[-1 for i in range(K+1)]
dp[0]=0
for i in range(n):
    for j in range(K+1):
        if dp[j]>=0:
            dp[j]=m[i]
        elif j<a[i] or dp[j-a[i]]<=0:
            dp[j]=-1
        else:
            dp[j]=dp[j-a[i]]-1
    #print(dp)
if dp[K]>=0:
    print("Yes")
else:
    print("No")
#print(dp)
