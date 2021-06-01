class SlidingWindowAggregation:
    def __init__(self, arr: list, op):
        self.a = arr
        self.n = len(arr)
        self.op = op
        self.l = 0
        self.r = 0
        self.back_l = 0
        self.front = []
        self.back = None

    def fold(self, s, t):
        """誰かがやる"""
        pass
