"""
{0,1,2,...,n-1}の部分集合の部分集合(空集合除く)の列挙

"""
n = int(input())
k = n
while k:
    # print(bin(k)[2:])
    k = (k-1)&n