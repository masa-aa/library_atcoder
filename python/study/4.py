import collections
n=int(input())
ans=0
d=1
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
c=prime_factorize(n)
print(c)
for i in range(len(c)):
    while c[i]-d>=0:
        c[i]-=d

        ans+=1
        d+=1
    if c[i]-d<0:
        d=1
print(ans)