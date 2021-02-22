# まだできてないよ WAだよ
# dfsをするがprevを書き換えられるため壊れる

from collections import deque


def cycle_detection(es: "隣接リスト", start: "始点" = 0):
    V = len(es)
    prev = [-1] * V  # 経路復元
    use = [0] * V
    que = deque()
    que.append(start)
    is_cycle = False
    while que:
        v = que.pop()
        use[v] = 1
        for e in es[v]:
            if use[e]:
                is_cycle = True
                prev[e] = v
                break
            else:
                prev[e] = v
                que.append(e)
        if is_cycle:
            break
    else:
        return []
    path = [e]
    t = prev[e]
    while t != e:
        path.append(t)
        t = prev[t]
    path.reverse()
    return path


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
es = [[] for _ in range(n)]
d = {}
# 入力
for i in range(m):
    start, end = map(int, input().split())
    # start -= 1; end -= 1
    es[start].append(end)
    d[(start, end)] = i

c = cycle_detection(es)
if c:
    c.append(c[0])
    res = []
    for i, j in zip(c, c[1:]):
        res.append(d[(i, j)])
    print(len(res))
    print(*res, sep="\n")
else:
    print(-1)
