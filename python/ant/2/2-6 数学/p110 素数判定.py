import math
def is_prime(n):
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True
n=int(input())
if is_prime(n):
    print("Yes")
else:
    print("No")
    
"""
Tips

以下の1, 2を比較する.

1
import math
for i in range(10**7):
	ans=math.sqrt(i)

2
for i in range(10**7):
	ans=i**0.5

1と2を10回ずつ回して平均を取ると
1. 2330ms
2. 2511ms
となったので1を採用している.
"""