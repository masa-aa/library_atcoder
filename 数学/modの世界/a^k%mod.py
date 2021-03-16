def modlist(a, Len, mod=1_000_000_007):
    """modlist[k]=(a**k)%mod (0<=k<=Len)を返す"""
    res = [0] * Len
    res[0] = 1
    for i in range(1, Len):
        res[i] = a * res[i - 1] % mod
    return res


if __name__ == '__main__':
    print(modlist(3, 5, 10))
