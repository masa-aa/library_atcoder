"""
「[a,b)にxを足す」というクエリをQ回をO(N+k)でする.
"""
n,q=map(int,input().split())
c=[0]*(n+1)
# Step1 
# [a,b)にxを足すとき, a番目に +x, b番目に -x
for i in range(q):
    a,b,x=map(int,input().split())
    c[a]+=x
    c[b]-=x

# Step2
# 累積和
for i in range(1,n+1):
    c[i]+=c[i-1]

print(*c)

"""
7 5
0 1 2
2 6 1
0 6 -1
3 5 3
2 2 1000
"""

"""
1 -1 0 3 3 0 0 0
"""