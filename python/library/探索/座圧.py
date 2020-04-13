"""
 座圧の対応表を返す {a:b,c:d,...}a→b, c→d,...
 定義域:list
"""
def compress(arr):
    *XS, = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)} 