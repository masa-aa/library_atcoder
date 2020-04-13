s=input()
num=""
a=[]
for i in range(len(s)):
    if s[i]==",":
        a.append(float(num))
        num=""
    else:
        num+=s[i]
a.append(float(num))
print(a)
print(sum(a))
