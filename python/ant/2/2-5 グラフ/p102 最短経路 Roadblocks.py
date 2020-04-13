"""
R本の道とN個の交差点がある街があります。道路は両方向に通行可能です。
1番の交差点からN番の交差点への2番目の最短路の長さを求めなさい。
ただし、二番目最短路とは、最短路よりも真に長いもののうちで最短のもののことを言います。
同じ道路を複数回通っても構いません。

制約
1<=N<=5000
1<=R<=10**5
"""
from heapq import heapify,heappop,heappush

#----標準入力なら-----
# n=int(input())
# r=int(input())
# G=[[] for i in range(n)]
# for i in range(r):
#     #from-to-cost
#     a,b,c=map(int,input().split())
#     a-=1
#     b-=1
#     G[a].append([b,c])
#     G[b].append([a,c])

n=4
r=4
G=[[[1,100]],
    [[0,100],[2,250],[3,200]],
    [[1,150],[3,100]],
    [[1,200],[2,100]]]


dist=[float("INF") for i in range(n)]
dist2=[float("INF") for i in range(n)]
p=[] #優先度付きキュー[to,cost]
heappush(p,[0,0])

while len(p)!=0:
    P=heappop(p)
    #print(P,dist,dist2)
    v=P[1]
    d=P[0]
    if dist2[v]<d:
        continue
    for i in range(len(G[v])):
        e=G[v][i]
        d2=d+e[1]
        #print(d2,e[0])
        if dist[e[0]] > d2:
            d2,dist[e[0]]=dist[e[0]],d2 #swap
            heappush(p,[dist[e[0]],e[0]])
        #print(e,dist,dist2)
        #print(d2)
        if dist2[e[0]]>d2 and dist[e[0]]<d2:
            #print("ok")
            dist2[e[0]]=d2
            heappush(p,[dist[e[0]],e[0]])

print(dist2[n-1])
            


