n=int(input())
a=list(map(int,input().split()))
dp=[[0]*3 for i in range(n)]
dp[0][0]=a[0]
dp[2][0]=dp[0][0]+a[2]
for i in range(3,n):
    dp[i][0]=dp[i-2][0]+a[i]
    dp[i][1]=max(dp[i-3][0],dp[i-2][1])+a[i]
    if i>=4:
        dp[i][2]=max(dp[i-4][0],dp[i-3][1],dp[i-2][2])+a[i]
ans=max(dp[n-3][0],dp[n-2][1],dp[n-1][0])