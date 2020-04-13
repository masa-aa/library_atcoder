"""
重さと価値がそれぞれw[i],v[i]であるようなn個の品物がある.
この中からちょうどk個選んだ時の単位重さあたりの価値の最大値を求めよ.

制約
1<=k<=n<=10^4
0<=w[i],v[i]<=10^6
|理論値-出力|<=10^-6
"""
#-------------------------------------------------------------------------------

# C(x) = 単位当たりの価値がx以上になるように選ぶことができる.
n,k=map(int,input().split())
w,v=[0]*n,[0]*n
for i in range(n):
    a,b=map(int,input().split())
    w[i],v[i]=a,b
y=[0]*n
def c(x):
    for i in range(n):
        y[i]=v[i]-x*w[i]
    return sum(sorted(y,reverse=True)[:k])>=0
l,r=0,10101010101
for i in range(100):
    mid=(l+r)/2
    if c(mid):
        l=mid
    else:
        r=mid
print(l)
"""
3 2
2 2
5 3
2 1
"""