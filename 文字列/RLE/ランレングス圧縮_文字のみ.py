# aaabaaccc -> [a, b, a, c]

def RLE(s):
    if not s:  # 空だと[]を返す.
        return []
    rle = []
    pre = s[0]
    cnt = 1
    for c in s[1:]:
        if c == pre:
            cnt += 1
        else:
            rle.append(pre)
            pre = c
            cnt = 1
    rle.append(pre)
    return rle


# print(RLE("aaabaaccc"))
