def dot(A, B, MOD=1000000007):
    # 行列の積 in Z/(mod Z)*(N*N)
    N, M, L = len(A), len(A[0]), len(B[0])
    res = [[0] * L for i in range(N)]
    for i in range(N):
        for j in range(L):
            s = 0
            for k in range(M):
                s = (s + A[i][k] * B[k][j]) % MOD
            res[i][j] = s
    return res


def matPow(A, x, MOD=1000000007):
    # A^x in Z/(mod Z)*(N*N)
    N = len(A)
    res = [[0] * N for i in range(N)]
    for i in range(N):
        res[i][i] = 1
    for i in range(x.bit_length()):
        if (x >> i) & 1:
            res = dot(res, A, MOD)
        A = dot(A, A, MOD)
    return res
