'''
食物連鎖(Union-Find木を用いる問題)
n匹の動物がいて1,2,...nと番号付けされている。動物はA,B,Cのいずれか。AはBを食べ、BはCを食べ、CはAを食べる。また、次の二つのうちいずれかの情報が順番にk個与えられる。
タイプ1 x,yは同じ種類の動物
タイプ2 xはyを食べる
しかしこの与えられたk個の情報が全て正しいとは限らない。k個の情報のうち正しくない(矛盾する)情報の個数を求めよ。
注意.正しくない情報が与えられたとき、その情報については以降の情報に対して一切考慮しない。(無視して考える)
'''
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
n,k=map(int,input().split())
t=[0]*k
x=[0]*k
y=[0]*k
for i in range(k):
 t[i],x[i],y[i]=map(int,input().split())
 x[i]-=1
 y[i]-=1
ans=0
h=UnionFind(3*n)
for i in range(k):
 print(ans,i)
 if x[i]<0 or n<=x[i] or y[i]<0 or n<=y[i]:
   ans+=1
   continue
 if t[i]==1:
   if h.isSameGroup(x[i],y[i]+n) or h.isSameGroup(x[i],y[i]+2*n):
     ans+=1
   else:
     h.Unite(x[i],y[i])
     h.Unite(x[i]+n,y[i]+n)
     h.Unite(x[i]+2*n,y[i]+2*n)
 else:
   if h.isSameGroup(x[i],y[i]) or h.isSameGroup(x[i],y[i]+2*n):
     ans+=1
   else:
     h.Unite(x[i],y[i]+n)
     h.Unite(x[i]+n,y[i]+2*n)
     h.Unite(x[i]+2*n,y[i])
print(ans)

