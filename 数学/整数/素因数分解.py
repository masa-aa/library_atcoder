def factorization(n: int) -> list:
    """Nを素因数分解(試し割り法)"""
    """2以上の整数N -> [e1, e2, ...]のリスト"""
    if n == 1:
        return []
    arr = []
    while n % 2 == 0:
        n //= 2
        arr.append(2)
    for i in range(3, n + 1, 2):
        if i * i > n:
            break
        while n % i == 0:
            n //= i
            arr.append(i)

    if n != 1:
        arr.append(n)

    return arr
