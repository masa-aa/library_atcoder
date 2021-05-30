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


def mid_point(p1, p2):
    '''
    中点を返す。
    '''
    x1, y1 = p1
    x2, y2 = p2
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return (x,y)


def is_collinear(p1,p2,p3):
    '''
    3点が同一直線上にあるかどうか。
    '''
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x1 - x2) * (y3 - y2) == (y1 - y2) * (x3 - x2)


def is_parallel(v1, v2):
    '''
    2つのベクトルが直線が平行かどうか。
    '''
    x1, y1 = v1
    x2, y2 = v2
    return x1 * y2 == y1 * x2


def get_vector(p1, p2):
    '''
    2点 p1, p2 に対し、ベクトル p2p1 を返す。
    '''
    vx = p2[0] - p1[0]
    vy = p2[1] - p1[1]
    return (vx, vy)


def get_intersection(l1, l2):
    '''
    2直線、l1, l2 の交点を返す。
    交点がない場合（共有点が無数にある場合も含む）は None を返す。
    したがって、共有点を求めたい場合は別に処理が必要。
    l1 = (p1, p2) で、2点 p1, p2 を通る直線。
    '''
    v1 = get_vector(*l1)
    v2 = get_vector(*l2)
    if is_parallel(v1, v2):
        return None
    a, b = l1[0]
    u, v = get_vector(*l1)
    c, d = l2[0]
    w, x = get_vector(*l2)

    s = ((a-c)*v - (b-d)*u) / (w*v - x*u)
    return (c+s*w, d+s*x)

def get_perpendicular_bisector(p1,p2):
    '''
    p1, p2 を両端とする線分の、垂直二等分線を返す。
    '''
    if p1 == p2:
        return None
    m = mid_point(p1, p2)
    a, b = get_vector(p1, p2)
    v = (-b, a)
    p = (m[0]+v[0], m[1]+v[1])
    return (m, p)


def get_circumcenter(p1,p2,p3):
    '''
    外心が存在すれば返す。
    '''
    if is_collinear(p1,p2,p3):
        return None
    l1 = get_perpendicular_bisector(p1, p2)
    l2 = get_perpendicular_bisector(p2, p3)
    return get_intersection(l1, l2)
