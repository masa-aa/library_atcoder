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

    def get(self, k):
        return self.arr[k]

    def __repr__(self):
        return "[{}]".format(", ".join(map(str, self.arr)))

    def top(self):
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


if __name__ == '__main__':
    a = DeletablePriorityQueue([4, 7, 7, 9, 1, 4, 5])
    print(a)
    for i in range(10):
        q, x = map(int, input().split())
        if q == 0:
            a.push(x)
        elif q == 1:
            print(a.pop())
        else:
            a.delete(x)
        print(a)
