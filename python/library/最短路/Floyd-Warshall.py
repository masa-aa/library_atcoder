"""
Floyd-Warshall法
頂点 n個
d[i][j]=iからjへの重み付き辺
が与えられた時、
dp[i][j]=iからjへの最短距離
（距離行列）を返す　O(n^3)
"""

n=int(input())
d=[list(map(int,input().split())) for i in range(n)]
def dis():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
dis()
for i in d:
    print(i)