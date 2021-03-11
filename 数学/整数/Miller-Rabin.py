def miller_rabin(n):
    """素数判定 log(n)"""
    if n < 2:
        return False

    base = [2, 7, 61] if n < 4_759_123_141 else \
           [2, 3, 5, 7, 11, 13, 17] if n < 341_550_071_728_321 else \
           [2, 3, 5, 7, 11, 13, 17, 19, 23] if n < 3_825_123_056_546_413_051 else \
           [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    if n in base:
        return True

    if n % 2 == 0:
        return False

    d = n - 1
    while d % 2 == 0:
        d //= 2

    for a in base:
        t = d
        y = pow(a, t, n)
        while t != n - 1 and y != 1 and y != n - 1:
            y = y * y % n
            t *= 2
        if y != n - 1 and t % 2 == 0:
            return False
    return True


if __name__ == "__main__":
    print(miller_rabin(2357))

# v = [2, 3, 5, 7, 325, 9375, 28178, 450775, 9780504, 1795265022]
# verify
# https://yukicoder.me/problems/no/3030
