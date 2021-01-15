"""
高速に何度も最小値（最大値）を取り出すときに有効
"""

from heapq import heappush, heapify, heappop
s = [13, 35, 1, 322, 10]
heapify(s)  # sをpriority-q化　O(n log(n))
a = heappop(s)  # 最小値を取り出す O(log(n))
print(a)  # 1
heappush(s, 123)  # 123をs(priority-q)に追加 O(log(n))

"""
これを利用してソートすることも可能 O(n log(n))
"""
print(s)
n = len(s)
t = [0] * n
for i in range(n):
    t[i] = heappop(s)
print(t)  # [10, 13, 35, 123, 322]
