"""
[Carmichael Number]
任意の1<x<nに対して, x^n≡x (mod n) が成り立つ素数以外のnを
Carmichael Numberといいます.
与えられた整数nがそれかどうか判定しなさい

!!制約!!
2<n<65000
"""
import math
def is_prime(n):
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True
m=int(input())
ans=True
for x in range(2,m):
    if (x**m-x)%m!=0 or is_prime(m):
        ans=False
        print("No")
        exit()
if ans:
    print("Yes")