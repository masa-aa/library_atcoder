"""
頂点数nと隣接リストesが与えられて, そのグラフが2部グラフか判定する
"""
import sys
sys.setrecursionlimit(100000000)
color = [0 for i in range(n)]


def dfs(v, c):
    color[v] = c
    for i in es[v]:
        if color[i] == c:
            return False
        if color[i] == 0 and not dfs(i, -c):
            return False
    return True
# グラフが連結の場合
# def is_bipartite():
#     return dfs(0,1)

# グラフが非連結の場合
# def is_bipartite():
#     for i in range(n):
#         if color[i]==0:
#             if not dfs(i, 1):
#                 return False
#     return True

# example
# n = 5 #連結の場合を使う
# es = [[1,2,3],[0,2],[0,1],[0,4],[3]]
# color = [0 for i in range(n)]
# is_bipartite() #Fasle

# n = 7 #非連結の場合を使う
# es = [[1,3],[0,2],[1,3],[0,2,4],[3],[6],[5]] # True
# color = [0 for i in range(n)]
# print(is_bipartite())
