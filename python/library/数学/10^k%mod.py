"""
make_modlist[k]=(10**k)%mod (0<=k<=Len)
を返す.
"""

def make_modlist(Len,mod):
    modlist=[0]*Len
    modlist[0]=1
    for i in range(1,Len):
        modlist[i]=10*modlist[i-1]%mod
    return modlist