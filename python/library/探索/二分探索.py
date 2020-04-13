"""
二分探索 リストLにeが存在すればTrue, 存在しなければFalseを返す.
"""

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

"""
昇順ソートされたリストaに昇順を崩さずxを挿入できる位置sを返す.
"""

from bisect import bisect_left
a=[1,3,5,7,9,11,13,15,17,19]
x=4
s = bisect_left(a,x)
s=2

