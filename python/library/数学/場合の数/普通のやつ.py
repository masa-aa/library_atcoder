#nPr
import math
def perm(n, r):
    return math.factorial(n) // math.factorial(n - r)


#nCr
import math
def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

#nHr
import math
def over(n, r):
    return math.factorial(n + r - 1) // (math.factorial(n - 1) * math.factorial(r))

"""
mod ver
"""
def framod(n, mod, a=1):
    for i in range(1,n+1):
        a=a * i % mod
    return a

def pow(n, r, mod):
    if r == 0: return 1
    if r%2 == 0:
        return pow(n*n % mod, r//2, mod) % mod
    if r%2 == 1:
        return n * pow(n, r-1, mod) % mod

def com(n, k, mod):
    a=framod(n, mod)
    b=framod(k, mod)
    c=framod(n-k, mod)
    return (a * pow(b, mod-2, mod) * pow(c, mod-2, mod)) % mod