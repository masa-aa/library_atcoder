class CumulativeSum2DDestroy:
    def __init__(self, c):
        """
        O(hw)
        入力 : c(リスト)
        cum[i][j] = [0, i] * [0, j]の和(面積)
        """
        # c[0] = []の時注意
        h = len(c)
        w = len(c[0])
        self.cum = c
        cur = c[0]
        for j in range(1, w):
            cur[j] += cur[j - 1]

        for i in range(1, h):
            prev = c[i - 1]
            cur = c[i]
            now = cur[0]
            cur[0] += prev[0]
            for j in range(1, w):
                cur[j], now = cur[j] + prev[j] + now, now + cur[j]

    def sum(self, a, b, x, y):
        """sum(a, b, x, y) = [a, b) * [x, y)の和(面積)"""
        b -= 1
        y -= 1
        if a > b or x > y:
            return 0
        if a == 0 and x == 0:
            return self.cum[b][y]
        if a == 0:
            return self.cum[b][y] - self.cum[b][x - 1]
        if x == 0:
            return self.cum[b][y] - self.cum[a - 1][y]
        return self.cum[b][y] - self.cum[b][x - 1] - self.cum[a - 1][y] + self.cum[a - 1][x - 1]

# なんか遅いなあ
