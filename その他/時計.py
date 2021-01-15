# H時M分が与えられて長針と短針のなす角Θ(0度<=Θ<180度)を返す

# 度数法 (0度<=Θ<180度)
def dos(H, M):
    H %= 12
    return min(abs(30 * H - 5.5 * M), 360 - abs(30 * H - 5.5 * M))


# 弧度法　(0<=Θ<π)
import math


def radi(H, M):
    H %= 12
    return math.pi * min(abs(30 * H - 5.5 * M), 360 - abs(30 * H - 5.5 * M)) / 180
