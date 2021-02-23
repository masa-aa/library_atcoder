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
    """2つのベクトルP, Qが平行かどうか"""
    a, b = P[0], Q[0]
    return all(a * j == i * b for i, j in zip(P, Q))


def is_orthogonal(P, Q):
    """2つのベクトルP, Qが垂直かどうか"""
    return P @ Q == 0


def same_line(a, b, c, d):
    """2つの線分(a, b), (c, d)が同一直線かどうか"""
    if not is_parallel(vector(a) - vector(b), vector(c) - vector(d)):
        return False
    return (a[0] - b[0]) * (c[1] - a[1]) == (a[1] - b[1]) * (c[0] - a[0])


def is_cross(a, b, c, d):
    """2つの線分(a, b), (c, d)が交差するかどうか"""
    if same_line(a, b, c, d):
        if a[0] == b[0]:
            s, t, u, v = a[1], b[1], c[1], d[1]
        else:
            s, t, u, v = a[0], b[0], c[0], d[0]
        if s > t:
            s, t = t, s
        if u > v:
            u, v = v, u
        return max(s, u) <= min(t, v)

    s = (a[0] - b[0]) * (c[1] - a[1]) - (a[1] - b[1]) * (c[0] - a[0])
    t = (a[0] - b[0]) * (d[1] - a[1]) - (a[1] - b[1]) * (d[0] - a[0])
    if s * t > 0:
        return False

    s = (c[0] - d[0]) * (a[1] - c[1]) - (c[1] - d[1]) * (a[0] - c[0])
    t = (c[0] - d[0]) * (b[1] - c[1]) - (c[1] - d[1]) * (b[0] - c[0])
    if s * t > 0:
        return False
    return True
