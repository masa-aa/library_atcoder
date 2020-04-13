def sumDigits(s):
    a=0
    for i in range(len(s)):
        try:
            a+=int(s[i])
        except ValueError:
            pass
    return a

print(sumDigits("21q"))
