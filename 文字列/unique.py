# aabbabccc -> ababcにする 出力はlist ※文字列に_が含まれてはならない.

def unique(s):
    prev = "_"
    ans=[]
    for c in s:
        if c != prev:
            ans.append(c)
            prev = c
    return ans
    # return "".join(ans)


# print(unique("aabbabccc"))