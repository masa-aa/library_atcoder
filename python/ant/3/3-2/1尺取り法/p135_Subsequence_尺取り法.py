"""
長さnの数列a[0],a[1],...a[n-1]と数列Sが与えられる.
連続する部分列で, その総和がS以上となるようなもののうち,
最小の長さを求めよ. 解が存在しない場合0を出力せよ.

制約
10<n<=10^5
0<a[i]<=10^4
S<10^8
"""
#-------------------------------------------------------------------------------
n,s=map(int,input().split())
a=list(map(int,input().split()))
ans=n+1
t,sm=0,0
for i in range(n):
    while t<n and sm<s:
        sm+=a[t]
        t+=1
    if sm<s:
        break
    ans=min(ans,t-i)
    sm-=a[i]
print(ans if ans<=n else 0)

"""
10 15
5 1 3 5 10 7 4 9 2 8
"""
"""
5 11
1 2 3 4 5
"""