"""
頂点数nと隣接リストesが与えられて, そのグラフが木か連結かどちらでもないか判定する
"""
import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
n=int(input()) # 頂点数
es=[[] for i in range(n)] # 隣接リスト
for i in range(n-1):
    a,b=map(int,input().split())
    es[a-1].append(b-1)
    es[b-1].append(a-1)
sw = [True for i in range(n)] # 頂点0とのパスが存在すればFalse, 存在しないならTrue と定義する
def dfs(v):
    sw[v] = False
    for i in es[v]:
        if sw[i]:
            dfs(i)
dfs(0)
# 連結か判定 ( 頂点0とのパスが存在しない頂点があれば連結でない )
for i in range(n):
    if sw[i]:
        print("not connected")
        exit()
# 木か判定 ( 連結で (頂点数-1) = (辺の数)　ならば木 )
# (隣接リストの要素数の和) = (辺の数)*2 であることに注意
m=0
for i in es:
    m+=len(i)
if m==2*(n-1):     
    print("tree")
else:
    print("connected but not tree")