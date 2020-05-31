"""
Pページある本がある. iページ目にはちょうど１つの事柄a[i]について書かれている.
本の中には同じ事柄が何度も書かれているので, 
この本の中の連続するページで全ての事柄をカバーしている部分を読むことにした.
各ページに書かれている事柄が与えられるので, 読まなければいけない最小のページ数を求めよ.

制約
1<=P<=10^6
1<=a[i]<=10^9
"""
#-------------------------------------------------------------------------------
p=int(input())
a=list(map(int,input().split()))
n=len(set(a))
cnt,k,ans=0,0,n
dic={}
for i in range(n):
    while cnt<n and k<p:
        if not(a[k] in dic) or dic[a[k]]==0:
            dic[a[k]]=1
            cnt+=1
        elif dic[a[k]]==0:
            dic[a[k]]+=1
        k+=1
    if cnt<n:
        break
    dic[a[i]]-=1
    if dic[a[i]]==0:
        cnt-=1
    ans=min(ans,k-i)
print(ans)

"""
5
1 8 8 8 1
"""