from random import randrange
from time import time


def heappush(a: list, k: int):
    n = len(a)
    a.append(k)
    while n and a[(n - 1) // 2] > a[n]:
        m = (n - 1) // 2
        a[m], a[n] = a[n], a[m]
        n = m


def heappop(a: list):
    a[0], a[-1] = a[-1], a[0]
    res = a.pop()
    n = len(a)
    m = 0
    limit = n // 2
    while m < limit:
        m2 = m + m + 1
        if m2 + 1 < n:
            if a[m2] < a[m2 + 1]:
                if a[m] > a[m2]:
                    a[m], a[m2] = a[m2], a[m]
                    m = m2
                else:
                    break
                if a[m] > a[m2 + 1]:
                    a[m], a[m2 + 1] = a[m2 + 1], a[m]
                    m = m2 + 1
                else:
                    break

        else:
            if a[m] > a[m2]:
                a[m], a[m2] = a[m2], a[m]
                m = m2
            else:
                break

    return res
