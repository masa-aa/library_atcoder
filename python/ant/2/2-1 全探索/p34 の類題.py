"""
長さNの整数列Aがあります。
Aの要素から一つ以上選んで総乗(全ての積)をとったとき、値がMに最も近くなるものを求めて下さい。
具体的には、以下の問題を解いてください。
・1以上N以下の相異なるk(k = 1, 2, ..., N)個の整数 p1 p2 ... pkに対して
　ΠApi=X としたとき、 |X-M|が最も小さくなるXを求めて下さい。
なお、答えが複数ある場合は値が最も小さいものを出力してください。

制約
・入力は全て整数で与えられる
・1≦N≦18
・1≦M≦1018
・-10≦Ai≦10
"""
#-------------------------------------------------------------------------------

import sys
sys.setrecursionlimit(1000000000)
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=[]
def dfs(i,s):
    if i==n:
        b.append(s)
        return None
    dfs(i+1,s)
    dfs(i+1,s*a[i])
dfs(0,1)
b.pop(0)
b.sort()
ans=10**18
p=0
for i in range(2**n -1):
    if abs(m-b[i])<ans:
        p=b[i]
        ans=m-b[i]
print(p)