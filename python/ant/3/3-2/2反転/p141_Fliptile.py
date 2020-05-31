"""
マスが0または1のM*Nのボードがある
あるマスを選ぶとそのマスと上下左右の合計5マスが反転する.
全てのマスを0に変えたいとき最小手数で各マスをひっくり返す方法を求めよ.
複数存在する場合,辞書順最小のものを, 存在しない場合は,"IMPOSSIBLE"を出力せよ.

制約
1<=N,M<=15
"""
#-------------------------------------------------------------------------------
from copy import deepcopy

n,m=map(int,input().split())
tile=[list(map(int,input().split())) for i in range(m)]
dx=[-1,0,1,0,0]
dy=[0,1,0,-1,0]
ans=[[0]*n for i in range(m)]
flip=[[0]*n for i in range(m)]
def get(x,y): # (x,y)の値を調べる(十字を調べればいい)
    c=tile[x][y]
    for i in range(5):
        p,q=x+dx[i],y+dy[i]
        if 0<=p<m and 0<=q<n:
            c+=flip[p][q]
    return c%2

def calc(): # 1行目固定で操作の最小回数を求める
    for i in range(1,m):
        for j in range(n):
            if get(i-1,j): #1つ上が1
                flip[i][j]=1
    for i in range(n):
        if get(m-1,i):
            return 1001 # 無理の時
    res=0 #反転回数をカウント
    for i in flip:
        res+=sum(i)
    return res

def solve():
    res=1001
    global flip
    for i in range(1<<n):
        flip=[[0]*n for i in range(m)]
        for j in range(n):
            flip[0][n-j-1]=i>>j&1
        k=calc()
        if k<res:
            ans=deepcopy(flip)
            res=k
    if res>1000:
        print("IMPOSSIBLE")
    else:
        for i in ans:
            print(*i)

solve()

"""
4 4
1 0 0 1
0 1 1 0
0 1 1 0
1 0 0 1
"""