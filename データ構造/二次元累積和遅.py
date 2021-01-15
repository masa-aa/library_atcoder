class CumulativeSum2D:
    def __init__(self, c):
        """
        O(hw)
        入力 : c(2次元リスト)
        cum[i + 1][j + 1] = [0, i] * [0, j]の和(面積)
        """
        # c[0] = []の時注意
        h = len(c)
        w = len(c[0])
        self.cum = [[0] * (w + 1) for i in range(h + 1)]
        for j in range(w):
            self.cum[1][j + 1] = self.cum[1][j] + c[0][j]
        for i in range(1, h):
            now = 0
            for j in range(w):
                now += c[i][j]
                self.cum[i + 1][j + 1] += self.cum[i][j + 1] + now

    def sum(self, a, b, x, y):
        """sum(a, b, x, y) = [a, b] * [x, y]の和(面積)"""
        if a > b or x > y:
            return 0
        return self.cum[b + 1][y + 1] - self.cum[b + 1][x] - self.cum[a][y + 1] + self.cum[a][x]
