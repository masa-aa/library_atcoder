"""
要約
リストkが与えられる. mが与えられて, あるkの要素a,b,c,d（a,b,c,dは同じでもいい)
についてm=a+b+c+d　と出来るか？
制約
1<=n<=50 1<=m,k_i<=10^8
"""
#-------------------------------------------------------------------------------

n=int(input())
m=int(input())
k  = list(map(int, input().split()))
ans=False
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                if k[a]+k[b]+k[c]+k[d]==m:
                    ans=True
if ans:
    print('Yes')
else:
    print('No')
