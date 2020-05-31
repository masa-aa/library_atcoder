from heapq import heappush,heapify,heappop
INF = 10**10

n,m = map(int,input().split())

es=[[] for _ in range(n)] # es[i] = (頂点iの(隣接する頂点,コスト)の組)
d = [INF]*n # 頂点sからの最短距離
prev=[-1]*n # 経路復元

# 入力
for i in range(m):
    a,b,c = map(int,input().split())
    a,b = a-1, b-1
    es[a].append((b,c))
    es[b].append((a,c)) # 無向グラフ


def dijkstra(s):
    v = -1
    que = [(0,s)]
    heapify(que)
    d[s] = 0
    while que:
        p = heappop(que)
        v = p[1]
        if d[v] < p[0]:
            continue
        for e in es[v]:
            if d[e[0]] > d[v] + e[1]:
                d[e[0]] = d[v] + e[1]
                heappush(que, (d[e[0]], e[0])) 
                prev[e[0]] = v
def get_path(t):
    path = []
    while t != -1:
        path.append(t)
        t = prev[t]
    path.reverse()
    return path
# dijkstra(0)
# print(d)