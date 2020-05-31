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
from bisect import bisect_left 
#昇順ソートされたリストaに昇順を崩さずxを挿入できる位置s(0-index)を返す.

n,s=map(int,input().split())
a=[0]+list(map(int,input().split()))
for i in range(1,n+1):
    a[i]+=a[i-1]
if a[n]<s:
    print(0)
ans=n
for i in range(n):
    if a[n]-a[i]<s:
        break
    #sum[t]-sum[i]>=sとなるtの最小値を求める.
    ans=min(ans,bisect_left(a,a[i]+s,i)-i)
print(ans)

"""
10 15
5 1 3 5 10 7 4 9 2 8
"""
"""
5 11
1 2 3 4 5
"""