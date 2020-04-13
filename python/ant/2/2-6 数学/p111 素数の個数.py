def sieve(n):
    is_prime = [True for _ in range(n)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    return is_prime
n=int(input())
a=sieve(n)
cnt=0
for i in a:
    if i:
        cnt+=1
print(cnt)