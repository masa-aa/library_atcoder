"""
d:=[[頂点i,頂点j,iからjへのコスト],...]
として,最小全域木のコストを返す.
"""

class UnionFind():
   def __init__(self, n):
       self.n = n
       self.root = [-1]*(n+1)
       self.rnk = [0]*(n+1)
   def Find_Root(self, x):
       if(self.root[x] < 0):
           return x
       else:
           self.root[x] = self.Find_Root(self.root[x])
           return self.root[x]
   def Unite(self, x, y):
       x = self.Find_Root(x)
       y = self.Find_Root(y)
       if(x == y):
           return
       elif(self.rnk[x] > self.rnk[y]):
           self.root[x] += self.root[y]
           self.root[y] = x
       else:
           self.root[y] += self.root[x]
           self.root[x] = y
           if(self.rnk[x] == self.rnk[y]):
               self.rnk[y] += 1
   def isSameGroup(self, x, y):
       return self.Find_Root(x) == self.Find_Root(y)
   def Count(self, x):
       return -self.root[self.Find_Root(x)]

def krascal(n, D):
    h = UnionFind(n)
    D.sort(key=lambda x: x[2])
    cnt = 0
    for x, y, c in D:
        if not h.isSameGroup(x, y):
            h.Unite(x, y)
            cnt += c
    return cnt


#--------------------------------------------------------------------------------------------
n=7
d=[[0, 1, 3], [1, 2, 2], [2, 3, 60], [3, 4, 3], [4, 5, 7], [5, 6, 9],  [2, 6, 100], [5,6,100]] 

print(krascal(n,d))
# >>> 84
