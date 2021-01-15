"""
根付き木に対し, その2頂点u,vの共通の祖先で最も近い所にあるものを
uとvのLCA(Lowest Common Ancedtor,共通最小祖先)と言う.
"""
# O((N + Q)log(n))解法 #N=10**6 としておく.

# 入力はすべて1-index
import sys
sys.setrecursionlimit(1000000000)
input = sys.stdin.readline
n = int(input())  # 頂点数
root = int(input()) - 1  # 根ノードの番号
es = [[] for i in range(n)]  # 隣接リスト
parent = [[-1] * n for i in range(21)]  # 親を2^k回辿って到達する頂点 (根を通り過ぎる場合は-1とする)
# floor(log2(10^k)) の値は以下の通り
# [(4, 14), (5, 17), (6, 20), (7, 24), (8, 27), (9, 30)]
depth = [0] * n  # 根からの深さ

for i in range(n - 1):
    a, b = map(int, input().split())
    es[a - 1].append(b - 1)
    es[b - 1].append(a - 1)

# depthとparentを確定させる.


def dfs(v, p, d):
    parent[0][v] = p
    depth[v] = d
    for i in es[v]:
        if i - p:
            dfs(i, v, d + 1)


def init():
    # parent[0]とdepthを初期化する
    dfs(root, -1, 0)
    # parent を初期化する(ダブリング法)
    for k in range(20):
        for v in range(n):
            if parent[k][v] < 0:
                parent[k + 1][v] = -1
            else:
                parent[k + 1][v] = parent[k][parent[k][v]]


def lca(u, v):
    if depth[u] > depth[v]:
        u, v = v, u
    # uとvの深さを合わせる
    for k in range(21):
        if (depth[v] - depth[u]) >> k & 1:
            v = parent[k][v]
    if u == v:
        return u
    # 二分探索でLCAを求める.
    for k in range(20, -1, -1):
        if parent[k][u] - parent[k][v]:
            u, v = parent[k][u], parent[k][v]  # 違ったら一気にショートカット
    return parent[0][u]


init()
q = int(input())
for i in range(q):
    u, v = map(int, input().split())
    print(lca(u - 1, v - 1) + 1)

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
