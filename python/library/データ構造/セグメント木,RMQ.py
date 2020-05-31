"""
セグメント木：蟻本P153
できること：a[i]の更新(O(log n))、a[L],...,a[R-1]の最小値など(O(log n))
入力：n,a(配列)
     'ide_ele' : 単位元(min:∞, 和:0, 積:1, gcd:0)
     'segfunc' : return min(x,y) とかにする
出力:'init(a)': 配列aで初期化。O(N)
     'update(k,x)': a[k]をxに変更 O(logN)
     'query(p,q)': [p,q)について "segfunc" したものを返す O(logN)
"""

#####segfunc######
def segfunc(x,y):
    return 


def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
    
def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
    
def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[p])
        if q&1 == 1:
            res = segfunc(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[p])
    else:
        res = segfunc(segfunc(res,seg[p]),seg[q])
    return res
n=int(input())
a=list(map(int,input().split()))
#####単位元######
ide_ele = 0 #変える
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num

#-------------------------------------------------------------------------------
# 実装例

# ####segfunc######
# def segfunc(x,y):
#     return min(x,y)


# def init(init_val):
#     #set_val
#     for i in range(n):
#         seg[i+num-1]=init_val[i]    
#     #built
#     for i in range(num-2,-1,-1) :
#         seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
    
# def update(k,x):
#     k += num-1
#     seg[k] = x
#     while k:
#         k = (k-1)//2
#         seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
    
# def query(p,q):
#     if q<=p:
#         return ide_ele
#     p += num-1
#     q += num-2
#     res=ide_ele
#     while q-p>1:
#         if p&1 == 0:
#             res = segfunc(res,seg[p])
#         if q&1 == 1:
#             res = segfunc(res,seg[q])
#             q -= 1
#         p = p//2
#         q = (q-1)//2
#     if p == q:
#         res = segfunc(res,seg[p])
#     else:
#         res = segfunc(segfunc(res,seg[p]),seg[q])
#     return res

n = 5
a = [10,3,5,7,9]

#####単位元######
ide_ele = 1000000007

#num:n以上の最小の2のべき乗
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num

init(a)
print(query(1,4)) #[1,4)での最小値
    #>> 3
update(3,2) #A[3]を2に変更
print(query(1,4)) #[1,4)での最小値
    #>> 2