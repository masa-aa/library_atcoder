"""
長い板からn個の板を切り出したい. 切り出そうとしている板の長さは,
L_1, L_2, ... ,L_n であり, 元の板の長さはちょうどこれの合計である.
板を切断するときその板の長さだけコストがかかる.
すべての板を切り出したとき, 最小のコストはいくらか.
 1<=n<=20000 1<L_i<=50000
 """
#-------------------------------------------------------------------------------

#注意 教科書とは別の解法　　O(n log(n))

import heapq as hq
n = int(input())
l = list(map(int, input().split()))
cost=0
hq.heapify(l)
for i in range(n-1):
    a=hq.heappop(l)+hq.heappop(l)
    cost+=a
    hq.heappush(l,a)
print(cost)
