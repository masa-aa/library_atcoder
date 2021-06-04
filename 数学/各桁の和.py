def digit_sum(n: int, k=10) -> int:
    """nをk進数表記した時の各桁の和を求める．"""
    res = 0
    while n:
        m = n // k
        res += n - m * k
        n = m
    return res
