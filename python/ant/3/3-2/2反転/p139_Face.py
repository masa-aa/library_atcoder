"""
N匹の牛が一列に並んでいる. 各牛は前か後ろを向いている. 全ての牛を前向きにしたい.
始めにKを設定して, 1回の操作で連続するちょうどK頭の向きを変えることができる.
全ての牛を前向きにするために必要な最小の操作回数Mと, それを達成する最小のKを求めよ.

制約
1<=N<=5000
F:前向き B:後ろ向き
"""
#-------------------------------------------------------------------------------

n=int(input())
s=input()
def calc(k):
    f=[0]*n # f[i]=区間[i,i+k-1]を反転させたか sum[i-k+1,i-1](f[i]) の偶奇を調べる
    now=0
    ans=0
    for i in range(n-k+1):
        if (now+(s[i]=="B"))&1:
            f[i]=1
            ans+=1
            now+=f[i]
        if i-k+1>=0:
            now-=f[i-k+1]
    for i in range(n-k+1,n):
        if (now+(s[i]=="B"))&1:
            return 100000
        if i-k+1>=0:
            now-=f[i-k+1]
    return ans
m=100000
k=1
for i in range(1,n):
    ans=calc(i)
    if ans<m:
        k=i
        m=ans
print(m,k)
"""
7
BBFBFBB
"""