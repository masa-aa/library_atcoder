def factorization(N):
    """Nを素因数分解(試し割り法)"""
    """2以上の整数N => [素因数1, 素因数2, ...]の2次元リスト"""
    if N == 1:
        return []
    arr = []
    temp = N
    if temp % 2 == 0:
        cnt = 0
        while temp % 2 == 0:
            cnt += 1
            temp //= 2
            arr.append(2)
    for i in range(3, N + 1, 2):
        if i * i > N:
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
