def comb(n, k, mod=1_000_000_007):
    """nCk (nが大きくてkが小さい) O(k+log(mod)), n < kで0を返す"""
    # comment：引数のmodを消してグローバルに置くと最適化で速くなると思う．
    if n < k or n < 0 or k < 0:
        return 0

    if n - k < k:
        k = n - k
    ans = 1
    inv = 1
    for i in range(1, k + 1):
        ans = ans * (n - k + i) % mod
        inv = inv * i % mod
    return ans * pow(inv, mod - 2, mod) % mod
