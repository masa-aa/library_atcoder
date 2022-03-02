def multiple_loops(loops: list):
    """
    各 k 対して, loops[k] 回ループする. itertools.productに似ている.
    """
    n = len(loops)
    d = [0] * n
    loop_count = 1
    for i in loops:
        loop_count *= i
    if 0 in loops:
        return
    yield tuple(d)
    for _ in range(loop_count - 1):
        d[0] += 1
        i = 0
        while i < n and d[i] == loops[i]:
            d[i] = 0
            i += 1
            d[i] += 1
        yield tuple(d)


if __name__ == '__main__':
    a = [1, 1, 2]
    for v in multiple_loops(a):
        print(v)
