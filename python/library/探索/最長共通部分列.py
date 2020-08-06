# seqの単調増加列の長さ
# パラメータ wider_sense:False=狭義(<), True:広義(<=)

def LIS(seq, wider_sense=False):
    from bisect import bisect_left, bisect_right
    f = bisect_right if wider_sense else bisect_left
    N = len(seq)
    INF = 1000000000000000000
    dp = [INF] * (N+1)
    for x in seq:
        dp[f(dp, x)] = x
    return f(dp, INF - 1)