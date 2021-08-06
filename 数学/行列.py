def dot(A: "Matrix", B: "Matrix"):
    """行列の積 (mod)"""
    N, M, L = len(A), len(A[0]), len(B[0])
    res = [[0] * L for i in range(N)]
    for i in range(N):
        for j in range(L):
            s = 0
            for k in range(M):
                s = (s + A[i][k] * B[k][j]) % mod
            res[i][j] = s
    return res


def matPow(A: "Matrix", x: int):
    """A^x (mod)"""
    N = len(A)
    res = [[0] * N for i in range(N)]
    for i in range(N):
        res[i][i] = 1
    for i in range(x.bit_length()):
        if (x >> i) & 1:
            res = dot(res, A)
        A = dot(A, A)
    return res


def dot_matvec(A: "Matrix", v: list):
    """A*v (mod)"""
    N = len(A)
    M = len(A[0])
    res = [0] * M
    for i in range(N):
        for j in range(M):
            res[i] += A[i][j] * v[j]
            res[i] %= mod
    return res


mod = 1000000007  # 設定する
