"""
fとxとdを与えてf(f(...f(x))) (d回)をO(log(d))で求める.
"""
f,d,n=[],10101,10
x=[i for i in range(n)]


from copy import copy
for _ in range(30):
    if d%2:
        for i in range(n):
            x[i]=f[x[i]]
    d//=2
    tmp=copy(f)
    for i in range(n):
        f[i]=tmp[tmp[i]]

# https://atcoder.jp/contests/abc013/submissions/11644388