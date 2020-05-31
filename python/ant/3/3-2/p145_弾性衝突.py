"""
n個の半径r(cm)のボールを用いた次のような実験を行う.

上空H(m)のところに筒を設置し,ボールを縦に入れる（下からi番目のボールは下端がH+2Riにある)
実験開始と同時に一番下のボールを落下させ以後1秒ごとに1つずつボールを落下させる.
空気抵抗などはなく,床や他のボールとは弾性衝突をする.
この実験の開始後T秒経過時点での各ボールの下端の高さを求めよ.
g=10m/s^2とする.

制約
1<=n<=100
1<=h<=10000
1<=r<=100
1<=T<=10000
"""
#-------------------------------------------------------------------------------
from math import sqrt
n,h,r,T=map(int,input().split())

def calc(T):
    if T<0:
        return h
    t=sqrt(h/5) #t=sqrt(2*h/g)
    k=T//t
    if k%2:
        return h-5*(k*t+t-T)**2
    else:
        return h-5*(T-k*t)**2
y=[0]*n
for i in range(n):
    y[i]=calc(T-i)
y.sort()
for i in range(n):
    print(y[i]+2*r*i/100,end=" ")
print()

"""
1 10 10 100
"""
"""
2 10 10 100
"""