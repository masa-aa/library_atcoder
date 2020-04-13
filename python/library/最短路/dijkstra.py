# 参考
# https://note.nkmk.me/python-scipy-shortest-path/
# https://kawap23.hatenablog.com/entry/2019/09/09/195909#課題

"""
頂点数N、辺の数M、Ai, Bi 間の重みがC_i
点1と点Xの最短経路
入力
N M
A0 B0 C0
A1 B1 C1
....
A(M-1) B(M-1) C(M-1)
X
"""
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

n, m = map(int, input().split())
edge = np.array([input().split() for _ in range(m)], dtype = np.int64).T
graph = csr_matrix((edge[2], (edge[:2] - 1)), (n, n))
x = int(input())

ans = dijkstra(graph, directed = False, indices = 0) #有向グラフの場合はdirected = True ,indicesは始点
print(int(ans[x-1]))
# print (type(ans))
# <class 'numpy.ndarray'>
# print (ans)
# [ 0.  2.  5.  7. 12.  8. 17.]
#------------------------------------------------------------------------------
# distance_mat, processors = dijkstra(graph, directed = False, indices = [0, 1], return_predecessors = True)
# print ('点0からの最短距離')
# print (distance_mat)

# print ('各点の直前の点')
# print (processors)