"""
Conscription(POJ No.3723)
N人の女とM人の男を徴兵したいと思います。
一人を徴兵するのには10000ドルの費用がかかりますが、
すでに親しい間柄の人が徴兵されている場合、
より安い費用で徴兵することが可能です。
いくつかの男女の間には１〜9999の親密度が定まっており、
ある人を徴兵する際の費用は、
10000―（すでに徴兵されている人のうちで最も高い親密度）となります。
このとき、適切な順番で徴兵を行うことにより、全員を徴兵するために必要な費用を最小化しなさい。

制約
1≤N,M≤10000
0≤R≤50000
0<d<10000
"""
class UnionFind():
   # 作りたい要素数nで初期化
   # 使用するインスタンス変数の初期化
   def __init__(self, n):
       self.n = n
       # root[x]<0ならそのノードが根かつその値が木の要素数
       # rootノードでその木の要素数を記録する
       self.root = [-1]*(n+1)
       # 木をくっつける時にアンバランスにならないように調整する
       self.rnk = [0]*(n+1)
   # ノードxのrootノードを見つける
   def Find_Root(self, x):
       if(self.root[x] < 0):
           return x
       else:
           # ここで代入しておくことで、後の繰り返しを避ける
           self.root[x] = self.Find_Root(self.root[x])
           return self.root[x]
   # 木の併合、入力は併合したい各ノード
   def Unite(self, x, y):
       # 入力ノードのrootノードを見つける
       x = self.Find_Root(x)
       y = self.Find_Root(y)
       # すでに同じ木に属していた場合
       if(x == y):
           return
       # 違う木に属していた場合rnkを見てくっつける方を決める
       elif(self.rnk[x] > self.rnk[y]):
           self.root[x] += self.root[y]
           self.root[y] = x
       else:
           self.root[y] += self.root[x]
           self.root[x] = y
           # rnkが同じ（深さに差がない場合）は1増やす
           if(self.rnk[x] == self.rnk[y]):
               self.rnk[y] += 1
   # xとyが同じグループに属するか判断
   def isSameGroup(self, x, y):
       return self.Find_Root(x) == self.Find_Root(y)
   # ノードxが属する木のサイズを返す
   def Count(self, x):
       return -self.root[self.Find_Root(x)]
n,m,r = map(int,input().split())
xyd = [tuple(map(int,input().split())) for i in range(r)]
xyd.sort(reverse=True, key=lambda x:x[2])
h = UnionFind(n+m) #男性は0~n-1, 女性はn~n+m-1とする
ai = 0
for i in xyd:
    if not h.isSameGroup(i[0],i[1]+n):
        h.Unite(i[0],i[1]+n)
        ai += i[2]
print(10000*(n+m) - ai)

"""
テストケース
5 5 8
4 3 6831
1 3 4583
0 0 6592
0 1 3063
3 3 4975
1 3 2049
4 2 2104
2 2 781

71071
"""