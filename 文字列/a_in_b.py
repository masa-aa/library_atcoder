B = 10 ** 9 + 7  # ハッシュの基数


def contain(a, b, mod=2 << 61 - 1):
    """ a は b に含まれているか"""
    len_a, len_b = len(a), len(b)
    if len_a > len_b:
        return False

    t = pow(B, len_a, mod)

    # a と b 最初のlen(a)文字に関するハッシュ値を計算
    hash_a, hash_b = 0, 0
    for i in range(len_a):
        hash_a = (hash_a * B + ord(a[i])) % mod
        hash_b = (hash_b * B + ord(b[i])) % mod

    # b の場所を1つずつ進めながらハッシュ値をチェック
    for i in range(len_b - len_a):
        if hash_a == hash_b:
            return True
        hash_b = (hash_b * B + ord(b[len_a + i]) - ord(b[i]) * t) % mod
    return hash_a == hash_b


# print(contain("ac", "ababac"))
