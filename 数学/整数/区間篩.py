# verifyしてない
def segment_sieve(l, r):
    """k in [l, r) が 素数かどうかを返す．アクセスはis_prime[l + k]"""
    n = int(r**.5) + 1
    base = [True] * n
    is_prime = [True] * (r - l)
    for i in range(2, n):
        if base[i]:
            for j in range(i * i, n, i):
                base[j] = False
            for j in range(max(2, (l + i - 1) // i * i), r, i):
                if i != j:
                    is_prime[j - l] = False
    return is_prime
