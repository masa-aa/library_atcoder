class vector:
    def __init__(self, P):
        P = list(P)
        self.n = len(P)
        self.P = P

    def __getitem__(self, k):
        return self.P[k]

    def __setitem__(self, k, x):
        self.P[k] = x

    def __add__(self, other):
        return vector(i + j for i, j in zip(self, other))

    def __iadd__(self, other):
        for i, e in enumerate(other):
            self.P[i] += e
        return self

    def __sub__(self, other):
        return vector(i - j for i, j in zip(self, other))

    def __isub__(self, other):
        for i, e in enumerate(other):
            self.P[i] -= e
        return self

    def __mul__(self, other):
        return vector(i * j for i, j in zip(self, other))

    def __matmul__(self, other):
        return sum(i * j for i, j in zip(self, other))

    def __imul__(self, k):
        for i in range(self.n):
            self.P[i] *= k
        return self

    def __rmul__(self, k):
        return vector(i * k for i in self)

    def __floordiv__(self, k):
        return vector(i // k for i in self)

    def __iter__(self):
        for v in self.P:
            yield v

    def __repr__(self):
        return "[{}]".format(" ".join(map(str, self)))


def is_parallel(P, Q):
    """2つのベクトルが平行かどうか"""
    a, b = P[0], Q[0]
    return all(a * j == i * b for i, j in zip(P, Q))


def is_orthogonal(P, Q):
    """2つのベクトルが垂直かどうか"""
    return P @ Q == 0


def is_cross(P, Q):
    
    pass


