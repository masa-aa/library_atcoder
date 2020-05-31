class Cum: # 累積和クラス
    def __init__(self,a):
        n = len(a)
        self.cum = [0]*(n+1)
        for i in range(1,n+1):
            self.cum[i]=a[i-1]+self.cum[i-1]
    def calc(self,i,j): # [i,j)の和を返す.
        return self.cum[j] - self.cum[i]

a = [1,2,3,4,5]
b = [2,3,5,7,11]
h = Cum(a)
f = Cum(b)
print(h.cum)
print(f.cum)
print(h.calc(1,4)) # 9