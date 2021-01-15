# aaabaaccc -> [3, 1, 2, 3]

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
            rle.append(cnt)
            pre = c
            cnt = 1
    rle.append(cnt)
    return rle


print(RLE("aaabaaccc"))
