"""
根付き木に対し, その2頂点u,vの共通の祖先で最も近い所にあるものを
uとvのLCA(Lowest Common Ancedtor,共通最小祖先)と言う.
"""
# O(NQ)解法

# 入力はすべて1-index
import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
n=int(input()) # 頂点数
root = int(input())-1 # 根ノードの番号
es=[[] for i in range(n)] # 隣接リスト
parent = [-1]*n # 親ノードの番号 (根ノードの親は-1とする)
depth = [0]*n # 根からの深さ

for i in range(n-1):
   a,b = map(int,input().split())
   es[a-1].append(b-1)
   es[b-1].append(a-1)

# depthとparentを確定させる.
def dfs(v,p,d):
    parent[v] = p
    depth[v] = d
    for i in es[v]:
        if  i-p:
            dfs(i,v,d+1)

def init():
    dfs(root, -1, 0)

def lca(u,v):
    while depth[u] > depth[v]:
        u = parent[u]
    while depth[v] > depth[u]:
        v = parent[v]
    print(u,v)
    while u-v:
        u = parent[u]
        v = parent[v]
        # print(u,v)
    return u

init()
q = int(input())
for i in range(q):
    u,v = map(int,input().split())
    print(lca(u-1,v-1)+1)

"""
8
1
1 2
1 3
2 4
2 5
5 7
8 5
3 6
3
4 7
8 6
5 8
"""