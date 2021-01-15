def is_prime(N):
    """nの素数判定"""
    if N == 1:
        return False
    if N > 3 and N % 2 == 0:
        return False
    for i in range(3, N + 1, 2):
        if i * i > N:
            return True
        if N % i == 0:
            return False
    return True


