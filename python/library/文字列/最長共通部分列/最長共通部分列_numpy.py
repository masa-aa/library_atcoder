import numpy as np

def longest_common_subsequence(S,T):
    LS = len(S); LT = len(T)
    if LS > LT:
        S, T = T, S
        LS, LT = LT, LS
    dp = np.zeros(LT + 1, np.int64)
    for s in S:
        equal = (s == T)
        prev = dp.copy()
        np.maximum(dp[1:], prev[:-1] + equal * 1, out=dp[1:])
        np.maximum.accumulate(dp, out=dp)
    return dp[-1]