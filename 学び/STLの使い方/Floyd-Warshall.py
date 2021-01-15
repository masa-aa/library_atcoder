"""
Floyd-Warshall法
頂点 n個
d[i][j]=iからjへの重み付き辺
が与えられた時、
dist[i][j]=iからjへの最短距離
（距離行列）を返す　O(n^3)
"""

from scipy.sparse.csgraph import floyd_warshall
import numpy as np

n, m = map(int, input().split())
d = np.zeros((n, n))
# 入力
for i in range(m):
    a, b, c = map(int, input().split())
    a, b = a - 1, b - 1
    d[a, b] = c
    d[b, a] = c
dist = floyd_warshall(d, directed=0).astype(int)
