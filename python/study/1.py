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
n,m=map(int,input().split())
a=list(map(int,input().split()))
h=UnionFind(n)
for i in range(m):
    x,y=map(int,input().split())
    h.Unite(x,y)
dic={}
k=0
for i in range(n):
    x=h.Find_Root(i)
    if x in dic:
        dic[x].add(i)
    else:
        dic[x]={i}
        k+=1
b=[sorted([a[j] for j in dic[i]]) for i in dic]
ans=0
c=[]
cnt=0
if k==1:
    print(0)
    exit()
for i in range(k):
    ans+=b[i][0]
    if len(b[i])>1:
        for j in b[i][1:]:
            c.append(j)
    else:
        cnt+=1
if cnt>2:
    print("Impossible")
    exit()
else:
    c.sort()
    ans+=sum(c[:k-2])
print(ans)
