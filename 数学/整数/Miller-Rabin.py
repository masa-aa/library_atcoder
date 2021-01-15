def Miller(N):
    """素数判定, 決定的アルゴリズム"""
    v = [2, 7, 61] if N < 4_759_123_141 else \
        [2, 3, 5, 7, 11, 13, 17] if N < 341_550_071_728_321 else \
        [2, 3, 5, 7, 11, 13, 17, 19, 23] if N < 3_825_123_056_546_413_051 else \
        [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if N < 2:
        return False
    if N in v:
        return True
    d = N - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for a in v:
        if pow(a, d, N) != 1:
            ok = True
            for r in range(s):
                if pow(a, d * 1 << r, N) == N - 1:
                    ok = 0
                    break
            if ok:
                return False
    return True


if __name__ == "__main__":
    print(Miller(10**30 + 57))

# v = [2, 3, 5, 7, 325, 9375, 28178, 450775, 9780504, 1795265022]
# verify
# https://yukicoder.me/problems/no/3030
