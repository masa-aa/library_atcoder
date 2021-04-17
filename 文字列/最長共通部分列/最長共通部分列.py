def longest_common_subsequence(s, t):
    n = len(t)
    dp = [0] * (n + 1)
    prev = [0] * (n + 1)
    for c in s:
        prev, dp = dp, prev
        for i in range(n):
            if c == t[i]:
                dp[i + 1] = prev[i] + 1
            else:
                dp[i + 1] = max(dp[i], prev[i + 1])
    return dp[-1]


def convert(s):
    return list(map(ord, s))
