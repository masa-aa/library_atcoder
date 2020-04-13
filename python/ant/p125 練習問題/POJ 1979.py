# http://poj.org/problem?id=1979

#W×Hのグリッドが与えられる.
#"." のマスは通ることができ、一方 "#" のマスは通ることができない.
#このとき、スタート地点 @ から到達可能なマスの数を答えよ。
#1≤W,H≤20

w,h=map(int, input().split())
s = [list(input()) for i in range(h)]
dx=[0,1,-1,0]
dy=[1,0,0,-1]
for i in range(h):
    if '@' in s[i]:
        y=s[i].index('@')
        x=i
        break
s[x][y]='#'
def dfs(a,b):
    s[a][b]='@'
    for i in range(4):
        nx=a+dx[i]
        ny=b+dy[i]
        if 0<=nx<h and 0<=ny<w and s[nx][ny]=='.':
            dfs(nx,ny)
ans=0
dfs(x,y)
for i in range(h):
    for j in range(w):
        if s[i][j]=='@':
            ans+=1
print(ans)
