def compress(arr):
    """座圧の対応表と逆対応表を返す {a:b,c:d,...} a -> b, c -> d, ..."""
    com = {e: i for i, e in enumerate(sorted(set(arr)))}
    rcom = list(com.keys())
    return com, rcom
