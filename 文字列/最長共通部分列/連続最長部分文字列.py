def LongestCommonSubstrings(s, t):
    """両方の文字列に含まれる文字列のうち最も長いものの長さ"""
    res = i = j = 0
    l = len(s)
    while i < l and j < l:
        if s[i:j + 1] in t:
            res = max(res, j - i + 1); j += 1
        else:
            i += 1

    return res


"""
ABRACADABRA
ECADADABRBCRDARA

5
"""
