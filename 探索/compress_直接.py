def compress(arr):
    """破壊的に座圧する."""
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
    for i in range(len(arr)):
        arr[i] = com[arr[i]]
    return arr
