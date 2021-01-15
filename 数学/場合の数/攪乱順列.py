def disturbance(N, mod=1000000007):
    """
    攪乱順列
    1,2,...,n を並び替えてできる順列のうち，
    全ての i=1,2,...,n に対して i 番目が i でないものの個数
    """
    a, prev = 1, 0
    if N <= 3:
        return max(N, 1) - 1

    for i in range(2, N):
        a, prev = i * (prev + a) % mod, a
    return a
