"""
前処理 : 二次元累積和 O(hw)
入力 : h(第一成分の長さ), w(第二成分の長さ), c(リスト)
cum[i][j]=(0,0)~(i,j)の和(面積)
"""
def cum_gen(h,w,c):
    cum = [[0]*w for i in range(h)]
    cum[0][0] = c[0][0]
    for j in range(1,w):
        cum[0][j] = cum[0][j-1] + c[0][j]
    for i in range(1,h):
        now = 0
        for j in range(w):
            now += c[i][j]
            cum[i][j] += cum[i-1][j] + now
    return cum
"""
計算パート O(1)
cum_calc(a,b,x,y)=(a,b)~(x,y)の和(面積)
"""
def cum_calc(a,b,x,y):
    if a>x or b>y:
        return 0
    if a==0 and b==0:
        return cum[x][y]
    if a==0:
        return cum[x][y]-cum[x][b-1]
    if b==0:
        return cum[x][y]-cum[a-1][y]
    return cum[x][y]-cum[x][b-1]-cum[a-1][y]+cum[a-1][b-1]
h,w=map(int,input().split())
c=[list(map(int,input().split())) for i in range(h)]
cum=cum_gen(h,w,c)
# print(cum_calc(1,2,2,3))