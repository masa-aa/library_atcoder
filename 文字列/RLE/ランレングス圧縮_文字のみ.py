# aaabaaccc -> [a, b, a, c]

def RLE(s):
    if not s:  # 空だと[]を返す.
        return []
    rle = []
    pre = s[0]
    for c in s[1:]:
        if c == pre:
            continue
        else:
            rle.append(pre)
            pre = c
    rle.append(pre)
    return rle


# print(RLE("aaabaaccc"))
