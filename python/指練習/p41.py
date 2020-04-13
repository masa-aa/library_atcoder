def isIn(s,t):
    if s in t or t in s:
        return True
    else:
        return False
print(isIn("abc","bcabcd"))
print(isIn("abde","bc"))

def isIn2(s,t):
    x=0
    if len(s)<=len(t):
        for i in range(len(t)):
            if t[i]==s[x]:
                x+=1
                if x==len(s):
                    return True
            else:
                x=0
        return False
    else:
        for i in range(len(s)):
            if s[i]==t[x]:
                x+=1
                if x==len(t):
                    return True
            else:
                x=0
        return False
print(isIn2("abc","bcabcd"))
print(isIn2("abde","bc"))
