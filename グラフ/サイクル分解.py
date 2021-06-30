class CycleDecomposition:
    """置換をサイクル分解する"""

    def __init__(self, rho: list, one_base=True):
        """
        rho : 置換を与えるリスト(コピーは生成しないので値が変わるのに注意)
        1-indexedかどうか
        """
        n = len(rho)
        if one_base:
            for i in range(n):
                rho[i] -= 1
        self.cycle_index = [-1] * n  # 何番目のサイクルに属するか
        self.index = [-1] * n  # サイクルで何番目の要素か
        self.cycle = []  # k番目のcycle
        k = 0
        for i in range(n):
            if self.cycle_index[i] >= 0:
                continue
            self.cycle_index[i] = k
            self.index[i] = 0
            cycle = [i]
            j = rho[i]
            c = 1
            while i != j:
                self.cycle_index[j] = k
                self.index[j] = c
                cycle.append(j)
                c += 1
                j = rho[j]
            k += 1
            self.cycle.append(cycle)
        self.one_base = one_base

    def step(self, k: int, x: int):
        """rhoのk回合成, rho^(k) (x) を求める."""
        x -= self.one_base
        cycle_num = self.cycle_index[x]
        size = len(self.cycle[cycle_num])
        k += self.index[x]
        return self.cycle[cycle_num][k % size] + self.one_base
