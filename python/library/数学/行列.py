# 行列の積

def dot(A,B):
    N,M,L = len(A),len(A[0]),len(B[0])
    res = [[0]*L for i in range(N)]
    for i in range(N):
        for j in range(L):
            for k in range(M):
                res[i][j] += A[i][k]*B[k][j]
    return res


# A^x

def matPow(A,x):
    N = len(A)
    res = [[0]*N for i in range(N)]
    for i in range(N):
        res[i][i] = 1
    for i in range(x.bit_length()):
        if (x>>i) & 1:
            res = dot(res,A)
        A = dot(A,A)
    return res