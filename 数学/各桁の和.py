def digit_sum(n: int, k=10) -> int:
    """nをk進数表記した時の各桁の和を求める．"""
    res = 0
    while n > 0:
        res += n % k
        n //= k
    return res

# print(digit_sum(1342))
# 1 + 3 + 4  +2 = 10
