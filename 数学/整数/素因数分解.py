def factorization(n: int) -> list:
    """Nを素因数分解(試し割り法)"""
    """2以上の整数N -> [e1, e2, ...]のリスト"""
    if n == 1:
        return []
    res = []
    while n % 2 == 0:
        n //= 2
        res.append(2)
    for i in range(3, n + 1, 2):
        if i * i > n:
            break
        while n % i == 0:
            n //= i
            res.append(i)

    if n != 1:
        res.append(n)

    return res
