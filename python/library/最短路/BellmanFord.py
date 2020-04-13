def BF(p,n,s):
    inf=float("inf")
    d=[inf for i in range(n)]
    d[s-1]=0
    for i in range(n+1):
        for e in p:
            if e[0]!=inf and d[e[1]-1]>d[e[0]-1]+e[2]:
                d[e[1]-1] = d[e[0]-1] + e[2]
        if i==n-1:t=d[-1]
        if i==n and t!=d[-1]:
            return [0,'inf']
    return list(map(lambda x:-x, d))

n,m=map(int, input().split())
a=[list(map(int, input().split())) for i in range(m)]
a=[[x,y,-z] for x,y,z in a]
print(BF(a, n, 1)[-1])
