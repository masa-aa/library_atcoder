n=int(input())  #数値入力 「N」だけの入力のとき
a,b=map(int, input().split())  #複数数値入力　「A B」みたいなスペース空いた入力のとき
c=list(map(int, input().split()))  #リスト入力 「a1 a2 a3 ...」みたいな配列のような入力のとき
s = [list(map(int, input().split())) for i in range(n)]# 二次元配列入力　二次元マップみたいな入力のとき

#2次元リストの宣言
L = [[0 for i in range(n)] for j in range(m)]

a=100
b=0.987654321
print('{0:06d}-{1:6f}'.format(a,b))  # 0埋めのときの出力
# 000100-0.987654

print(*c)  #リスト出力
for i in [['#','.','#'],['#','#','#']]:print(*i, sep='')
#二次元リストで間を詰めたもの

s.sort(reverse=True, key=lambda x:x[1]) #二次元リストを2つ目に関して逆ソート
s,t=0,0
(t+s-1)//s #t/sの切り上げ

import time
t1 = time.time()
#計測する内容
t2 = time.time()
t = t2-t1
print(t)

l = [n*2 for n in l] #リストを2倍
s[::-1] #文字列の反転

1000000007 #10^9+7
998244353

if  True  :
    print('Yes')
else:
    print('No')

if a>b:a=b #a=min(a,b)