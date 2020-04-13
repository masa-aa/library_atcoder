"""
無向グラフGについて、Gの頂点数と隣接リストがあたえられる。
Gが二部グラフか判定せよ。
つまり隣接する頂点同士が違う色になるように、頂点に色を塗っていき、
2色以内で全ての頂点を塗ることができるか判定せよ。
ただしGはループや多重辺は持たないとする。

制約
1<=n<=1000

入力
N
ES[1][1]...ES[1][M_1]
.
.
.
ES[N][1]...ES[N][M_N]
"""

import sys
sys.setrecursionlimit(100000000) #今回は再帰回数が高々1000なのでいらない


n = int(input())
es = [list(map(int,input().split())) for i in range(n)]
color = [0 for i in range(n)]
def dfs(v, c):
    color[v] = c
    print(color)
    for i in es[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True
for i in range(n):
    if color[i] == 0:
        if not dfs(i, 1):
            print("No")
            exit()
print("Yes")

"""
頂点と辺をちょうど一度ずつ見ているので、計算量はO(|V|+|E|)
|E|<=n*(n-1)//2 であることに注意するとTLEしないことがわかる。
"""