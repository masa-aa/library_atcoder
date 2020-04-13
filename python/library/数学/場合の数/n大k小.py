# nが大きくてkが小さい O(k*log(mod))

mod=10**9+7
def comb(n,k):
    ans=1
    for i in range(1,k+1):
        ans=ans*(n-k+i)%mod
        ans=ans*pow(i,mod-2,mod)%mod
    return ans