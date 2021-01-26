def combs(n):
    """
        {0, 1, 2, ..., n - 1} (= 2^n - 1)
        の部分集合の部分集合(空集合除く)の列挙
    """
    comb = n
    while comb:
        yield comb
        comb = (comb - 1) & n
    yield 0  # 空集合を含めるとき


if __name__ == "__main__":
    for v in combs(13):
        print(v, bin(v)[2:])
