def longest_common_subsequence(S, T):
    LS = len(S); LT = len(T)
    if LT > LS:
        S, T = T, S
        LS, LT = LT, LS
    dp = [0] * (LT + 1)
    for s in S:
        dp_pre=dp[:]
        for j, t in enumerate(T):
            if s == t:
                dp[j + 1] = dp_pre[j] + 1
            elif dp[j + 1] < dp[j]:
                dp[j + 1] = dp[j]
    return dp[-1]

