# aabbabccc -> abcにする 出力はlist

# Python 3.7から順序関係が保証される
def get_different(s):
    return list(dict.fromkeys(s))
    #return "".join(dict.fromkeys(s))



print(get_different("aabbabccc"))