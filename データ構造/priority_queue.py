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
    while True:
        m2 = m + m + 1
        if m2 + 1 < n:
            if a[m2] < a[m2 + 1]:
                if a[m] > a[m2]:
                    a[m], a[m2] = a[m2], a[m]
                    m = m2
                else:
                    break
            else:
                if a[m] > a[m2 + 1]:
                    a[m], a[m2 + 1] = a[m2 + 1], a[m]
                    m = m2 + 1
                else:
                    break

        elif m2 < n:
            if a[m] > a[m2]:
                a[m], a[m2] = a[m2], a[m]
                m = m2
            else:
                break

        else:
            break

    return res


def test_push():
    a = []
    for i in rand:
        heappush(a, i)
    return a


def test_pop(a):
    k = 0
    while a:
        k += heappop(a)
    return k


n = 10**6
rand = [randrange(0, 10 ** 9) for _ in range(n)]

start = time()
a = test_push()
end = time()
print(f"my_push, {end-start} sec")

start = time()
test_pop(a)
end = time()

print(f"my_pop, {end-start} sec")

from heapq import heappush, heappop

start = time()
a = test_push()
end = time()
print(f"python_push, {end-start} sec")

start = time()
test_pop(a)
end = time()
print(f"python_pop, {end-start} sec")
