MOD = 10**9+7 #素数 変える場所 
class ModInt:
    def __init__(self, x):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)

    __repr__ = __str__

    def __add__(self, other):
        return (
            ModInt(self.x + other.x) if isinstance(other, ModInt) else
            ModInt(self.x + other)
        )

    def __sub__(self, other):
        return (
            ModInt(self.x - other.x) if isinstance(other, ModInt) else
            ModInt(self.x - other)
        )

    def __mul__(self, other):
        return (
            ModInt(self.x * other.x) if isinstance(other, ModInt) else
            ModInt(self.x * other)
        )

    def __truediv__(self, other):
        return (
            ModInt(
                self.x * pow(other.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(self.x * pow(other, MOD - 2, MOD))
        )

    def __pow__(self, other):
        return (
            ModInt(pow(self.x, other.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(self.x, other, MOD))
        )

    __radd__ = __add__

    def __rsub__(self, other):
        return (
            ModInt(other.x - self.x) if isinstance(other, ModInt) else
            ModInt(other - self.x)
        )

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return (
            ModInt(
                other.x * pow(self.x, MOD - 2, MOD)
            ) if isinstance(other, ModInt) else
            ModInt(other * pow(self.x, MOD - 2, MOD))
        )

    def __rpow__(self, other):
        return (
            ModInt(pow(other.x, self.x, MOD)) if isinstance(other, ModInt) else
            ModInt(pow(other, self.x, MOD))
        )
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

"""
使い方
https://qiita.com/wotsushi/items/c936838df992b706084c
"""
# A, B = map(ModInt, (map(int, input().split())))
# print(A / B)

# A = ModInt(int(input()))
# print((1 + A)**3)

# N = int(input())
# print(sum(ModInt(i)**2 for i in range(1, N + 1)))