class CumulativeSum2D:
    def __init__(self, c):
        """
        O(hw)
        入力 : c(リスト)
        cum[i][j] = [0, i] * [0, j]の和(面積)
        """
        # c[0] = []の時注意
        h = len(c)
        w = len(c[0])
        self.cum = [[0] * w for i in range(h)]
        self.cum[0][0] = c[0][0]
        for j in range(1, w):
            self.cum[0][j] = self.cum[0][j - 1] + c[0][j]
        for i in range(1, h):
            now = 0
            for j in range(w):
                now += c[i][j]
                self.cum[i][j] += self.cum[i - 1][j] + now

    def sum(self, a, b, x, y):
        """sum(a, b, x, y) = [a, b] * [x, y]の和(面積)"""
        if a > b or x > y:
            return 0
        if a == 0 and x == 0:
            return self.cum[b][y]
        if a == 0:
            return self.cum[b][y] - self.cum[b][x - 1]
        if x == 0:
            return self.cum[b][y] - self.cum[a - 1][y]
        return self.cum[b][y] - self.cum[b][x - 1] - self.cum[a - 1][y] + self.cum[a - 1][x - 1]


# h, w = map(int, input().split())
# c = [list(map(int, input().split())) for i in range(h)]
# cum = cum_gen(h, w, c)
# print(cum_calc(1, 1, 1, 1))
