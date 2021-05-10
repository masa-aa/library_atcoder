def compress(arr):
    """座圧の対応表と逆対応表を返す {a:b,c:d,...} a -> b, c -> d, ..."""
    rcom = sorted(arr)
    m = 0
    prev = -9223372036854775808
    for val in rcom:
        if val != prev:
            rcom[m] = val
            prev = val
            m += 1
    for _ in range(len(rcom) - m):
        rcom.pop()

    com = {e: i for i, e in enumerate(rcom)}
    return com, rcom
