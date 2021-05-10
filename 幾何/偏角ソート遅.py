# atan2でsortしろ
from functools import cmp_to_key


def ort(p):
    x, y = p
    if y > 0:
        return 1 if x > 0 else 2
    return 3 if x < 0 else 4


def ort2(p):
    """library checker"""
    x, y = p
    if y >= 0:
        return 1 if x >= 0 else 2
    return -1 if x < 0 else 0


def cross(p, q):
    x0, y0 = p
    x1, y1 = q
    return x0 * y1 - x1 * y0


def cmp(p, q):
    o1 = ort(p); o2 = ort(q)
    if p == q:
        return 0
    if o1 == o2:
        if cross(p, q) > 0:
            return - 1
        else:
            return 1
    if o1 < o2:
        return - 1
    return 1


CMP = cmp_to_key(cmp)


def argment_sort(arr):
    return sorted(arr, key=CMP)
