"""
整数a_1, a_2, ... ,a_nが与えられる.
その中からいくつか選び, ちょうどkにすることが出来るか判定せよ.
1<=n<=20
|a_i|<=10^9 
|k|<=10^9
"""
n,k = map(int,input().split())
a = list(map(int, input().split()))

for i in range(2**n):
    Sum = 0
    for j in range(n):
        if (i >> j) & 1:
            Sum += a[j]
    if Sum == k:
        print("Yes")
        exit()
print("No")

"""
test case 1

20 127
1 2 3 -4 5 6 7 8 9 10 11 12 11 10 9 8 8 5 10 -20

# Yes
"""

"""
test case 2

4 15
1 2 4 7

# No
"""