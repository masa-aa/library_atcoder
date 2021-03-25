from heapq import heappush, heapify, heappop


class DeletablePriorityQueue:
    """削除可能なPriorityQueue． popが償却log(n)"""

    def __init__(self, arr=[]):
        self.dic = {}
        for val in arr:
            if val in self.dic:
                self.dic[val] += 1
            else:
                self.dic[val] = 1
        heapify(arr)
        self.arr = arr

    def __getitem__(self, k):  # 非推奨
        return self.arr[k]

    def __repr__(self):  # 非推奨
        return "[{}]".format(", ".join(map(str, self.arr)))

    def __iter__(self):  # 非推奨
        for i in self.arr:
            yield i

    def __bool__(self):
        while self.arr and not self.dic[self.arr[0]]:
            heappop(self.arr)
        return bool(self.arr)

    def top(self):
        while not self.dic[self.arr[0]]:
            heappop(self.arr)
        return self.arr[0]

    def push(self, k):
        heappush(self.arr, k)
        if k in self.dic:
            self.dic[k] += 1
        else:
            self.dic[k] = 1

    def pop(self):
        k = heappop(self.arr)
        while not self.dic[k]:
            k = heappop(self.arr)
        self.dic[k] -= 1
        return k

    def delete(self, k):
        self.dic[k] -= 1
        if self.arr[0] == k:
            heappop(self.arr)

# https://atcoder.jp/contests/abc128/submissions/21253262
# SortedListより遅い
