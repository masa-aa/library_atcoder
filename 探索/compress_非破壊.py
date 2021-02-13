def compress(arr):
    """座圧の対応表を返す {a:b,c:d,...} a -> b, c -> d, ..."""
    return {e: i for i, e in enumerate(sorted(set(arr)))}
