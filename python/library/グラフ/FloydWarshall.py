INF = 10**10
n,m = map(int,input().split())
d = [[INF]*n for i in range(n)] 
# 入力
for i in range(m):
    a,b,c = map(int,input().split())
    a,b = a-1, b-1
    d[a][b] = c
    d[b][a] = c # 無向グラフ
for i in range(n):
    d[i][i] = 0

def FW():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])