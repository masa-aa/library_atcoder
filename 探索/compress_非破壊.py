def compress(arr):
    """座圧の対応表を返す {a:b,c:d,...}a→b, c→d,..."""
    *XS, = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)}
