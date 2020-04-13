#大きさがN*Mのが与えられる. 迷路は通路と壁からできており,
#1ターンに隣接する上下左右4マスの通路へ移動することができる.
#スタートからゴールまで移動するのに必要な最小ターン数を求めよ.
#ただし, スタートからゴールまで移動できると仮定する.
#1<=n,m<=100
# '#', '.', 'S', 'G'はそれぞれ, 壁, 通路, スタート, ゴールを表す.
from collections import deque
q=deque([])
dx=[-1,0,1,0]
dy=[0,1,0,-1]
n,m=map(int,input().split())
s = [list(input()) for i in range(n)]
for i in range(n):
    if 'S' in s[i]:
        sy=s[i].index('S')
        sx=i
        break
for i in range(n):
    if 'G' in s[i]:
        gy=s[i].index('G')
        gx=i
        break
d=[[10**8 for i in range(m)] for j in range(n)]
q.append([sx,sy])
d[sx][sy]=0
while q:
    p=q.popleft()
    if p[0]==gx and p[1]==gy:
        break
    for i in range(4):
        nx=p[0]+dx[i]
        ny=p[1]+dy[i]
        if 0<=nx<n and 0<=ny<m and s[nx][ny]!='#' and d[nx][ny]==10**8:
            q.append([nx,ny])
            d[nx][ny]=d[p[0]][p[1]]+1
print(d[gx][gy])
for i in d:
    print(*i)