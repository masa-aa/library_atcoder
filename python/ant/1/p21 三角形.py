"""
n本の棒の中から三本選んで最大の周長を求めよ.
3<=n<=100
1<=a_i<=10^6
"""

#-------------------------------------------------------------------------------

n=int(input())
a=list(map(int, input().split()))
a.sort(reverse=True)
ans=False
for i in range(n-2):
    if a[i]<a[i+1]+a[i+2]:
        print(a[i]+a[i+1]+a[i+2])
        ans=True
        break
if ans:
    print(0)
