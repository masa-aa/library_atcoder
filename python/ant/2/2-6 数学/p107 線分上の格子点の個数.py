"""
平面の2つの格子点P1=(x1,y1), P2=(x2,y2)が与えられる.
線分P1, P2上にはP1, P2以外にいくつの格子点が存在するか？

制約
|x1|,|x2|,|y1|,|y2|<=10^9
"""
def gcd(x,y):
    if y==0:
        return x
    return gcd(y, x%y)

x1,y1,x2,y2=map(int,input().split())

if x1 == x2 and y1 == y2:
    print(0)
else:
    print( gcd(abs(x2-x1), abs(y2-y1)) - 1 )

"""
入力例
1 11 5 3
# 3
3 3 3 3
# 0
"""