# aaabaaccc -> [(a,3),(b,1),(a,2),(c,3)]

def RLE(s):
    rle = []
    pre = s[0]
    cnt = 1
    for c in s[1:]:
        if c == pre:
            cnt += 1
        else:
            rle.append((pre, cnt))
            pre = c
            cnt = 1
    rle.append((pre, cnt))
    return rle


# print(RLE("aaabaaccc"))