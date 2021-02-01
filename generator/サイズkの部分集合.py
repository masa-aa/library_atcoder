def k_combs(n, k):
    """
    {0, 1, 2, ..., n - 1} (= 2^n - 1) 
    に含まれるサイズ k の部分集合の列挙
    """
    comb = (1 << k) - 1
    p = 1 << n
    while comb < p:
        yield comb
        x = comb & -comb
        y = comb + x
        comb = ((comb & ~y) // x >> 1) | y
