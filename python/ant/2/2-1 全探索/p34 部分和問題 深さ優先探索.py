#整数a_1, a_2, ... ,a_nが与えられる.
#その中からいくつか選び, ちょうどkにすることが出来るか判定せよ.
#1<=n<=20 |a_i|<=10^9 |k|<=10^9


import sys
sys.setrecursionlimit(1000000000)

n,k=map(int,input().split())
a=list(map(int, input().split()))

def dfs(i,s):
    if i==n:
        return s==k
    if dfs(i+1,s):
        return True
    if dfs(i+1,s+a[i]):
        return True
    return False
print(dfs(0,0))
