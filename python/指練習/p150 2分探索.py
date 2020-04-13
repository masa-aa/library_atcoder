def search(L,e):
    def bsearch(L,e,l,h):
        if h==l:
            return L[l]==e
        m=(h+l)//2
        if L[m]==e:
            return True
        elif L[m]>e:
            if l==m:
                return False
            else:
                return bsearch(L,e,l,m-1)
        else:
            return bsearch(L,e,m+1,h)
    if len(L)==0:
        return False
    else:
        return bsearch(L,e,0,len(L)-1)

n,x=map(int,input().split())
a=list(map(int,input().split()))
print(search(a,x))
