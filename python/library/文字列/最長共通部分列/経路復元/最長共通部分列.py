def longest_common_subsequence(S, T):
    LS = len(S); LT = len(T)
    dp = [[0] * (LT + 1) for _ in range(LS + 1)]
    for i, s in enumerate(S):
        for j, t in enumerate(T):
            if s == t:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp
    

def reconstruct_LCS(S, T, dp):
    tmp = []
    i, j = len(S), len(T)
    while i and j:
        if S[i - 1] == T[j - 1]:
            i, j = i - 1, j - 1
            tmp.append(S[i])
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(tmp))

