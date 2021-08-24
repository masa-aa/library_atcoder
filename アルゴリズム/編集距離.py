def levenshtein_distance(s: list or str, t: list or str) -> int:
    """ s と t の編集距離"""
    n = len(s)
    m = len(t)
    dp = list(range(m + 1))
    for i in range(n):
        dp[0] = i
        q = i
        for j in range(m):
            p = q
            q = dp[j + 1]
            if s[i] == t[j]:
                dp[j + 1] = p
            else:
                dp[j + 1] = min(q, dp[j], p) + 1

    return dp[m]
