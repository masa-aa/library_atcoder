def fac_init(_n=2_000_000, mod=1_000_000_007):
    """"fac[k] = k! % mod"""
    _n += 10
    fac = [1] * _n
    for i in range(1, _n):
        fac[i] = fac[i] * i % mod
    return fac


fac = fac_init()
