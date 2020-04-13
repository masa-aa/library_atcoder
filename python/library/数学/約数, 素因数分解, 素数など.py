"""
目次：約数列挙、最大公約数、最小公倍数、素因数分解、素数判定、エラトステネスの篩
"""



"""nの約数列挙"""
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()　#小さい順位欲しいとき
    return divisors


"""a,bの最大公約数"""
def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

"""a,bの最小公倍数"""
def lcm(a,b):
    return a*b//gcd(a,b)


"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
#複数回ver
n=int(input())
def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return table
Sieve=sieve(int(n**0.5)+1)
def m_factorization(n):
    arr = []
    temp = n
    for i in Sieve:
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr
#1回ver
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5)+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
factorization(24)

## [[2, 3], [3, 1]]
##  24 = 2^3 * 3^1


"""nの素数判定"""
import math
def is_prime(n):
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True

"""
エラトステネスの篩
1~nまで素数かどうかと1~nまでの素数の表
"""

def sieve(n):
    is_prime = [True for _ in range(n)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return is_prime, table
