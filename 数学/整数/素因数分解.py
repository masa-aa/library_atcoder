def factorization(n: int) -> list:
    """Nを素因数分解(試し割り法)"""
    """2以上の整数N -> [e1, e2, ...]のリスト"""
    if n == 1:
        return []
    arr = []
    temp = n
    if temp % 2 == 0:
        cnt = 0
        while temp % 2 == 0:
            cnt += 1
            temp //= 2
            arr.append(2)
    for i in range(3, n + 1, 2):
        if i * i > n:
            break
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
                arr.append(i)

    if temp != 1:
        arr.append(temp)

    return arr
