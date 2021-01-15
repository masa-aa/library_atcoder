from math import log
def prime_count(n):
    def isok(x):
        return x > n * log(x)
    def bisect(ng, ok):
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if isok(mid):
                ok = mid
            else:
                ng = mid
        return ok
    if n == 1:
        return 2
    x = bisect(2, n * n) + 1
    is_prime = [True] * x
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(x ** 0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i + i, x, i):
            is_prime[j] = False
    prime_list = [i for i in range(x) if is_prime[i]]
    return prime_list[n - 1]