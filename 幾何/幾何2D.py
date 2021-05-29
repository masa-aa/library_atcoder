class vector:
    def __init__(self, *P):
        self.x, self.y = P

    def __lt__(self, other):
        o1 = self.ort(); o2 = other.ort()
        if o1 == o2:
            return self.cross(other) > 0
        return o1 < o2

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return vector(self.x * other.x, self.y * other.y)

    def __matmul__(self, other):
        return self.x * other.x + self.y * other.y

    def __imul__(self, k):
        self.x *= k
        self.y *= k
        return self

    def __rmul__(self, k):
        self.x *= k
        self.y *= k
        return self

    def __floordiv__(self, k):
        self.x //= k
        self.y //= k
        return self

    def __iter__(self):
        yield self.x
        yield self.y

    def __repr__(self):
        return "[{}]".format(" ".join(map(str, self)))

    def dot(self, p):
        """内積"""
        return self @ p

    def cross(self, other):
        """外積"""
        return self.x * other.y - self.y * other.x

    def ort(self):
        """象限"""
        # 座標軸上 を初めに除く
        if not (self.x and self.y):
            return 0
        if self.y > 0:
            return 1 if self.x > 0 else 2
        return 3 if self.x < 0 else 4


def is_parallel(P, Q):
    """2つのベクトルP, Qが平行かどうか"""

    return P.cross(Q) == 0


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
