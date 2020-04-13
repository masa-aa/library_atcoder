"""
[区間内の素数の個数]
与えられたa,bに対して区間[a,b)には何個ありますか

!!制約!!
a<b<=10^^12
b-a<=10^6
"""
### is_prime[i-a]=True <=> iが素数

def segment_seive(a,b):
    ass=[]
    is_prime=[True for _ in range(b-a)]
    is_prime_small=[True for _ in range(int(b**0.5)+1)]

    for i in range(2,int(b**0.5)):
        if is_prime_small[i]:
            j=2*i
            while j**2<b:    ### [2,√b)の篩
                is_prime_small[j]=False
                j+=i
            j=max(2*i,((a+i-1)//i)*i)
            while j<b:　　　### [a,b)の篩
                is_prime[j-a]=False
                j+=i
    for i in range(len(is_prime)):
        if is_prime[i]:　　　　### is_prime[i]=True <=> a+iが素数
            ass.append(a+i)
    if ass[0]==1:  ### 1は素数じゃないので抜く
        del ass[0]
    return ass

x,y=map(int,input().split())
print(len(segment_seive(x,y)))