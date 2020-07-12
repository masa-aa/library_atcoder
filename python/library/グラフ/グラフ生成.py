# デバック用グラフ
from random import randint


def make_line(n):  # 直線グラフ
    es = [[] for _ in range(n)]
    for i in range(n - 1):
        es[i].append(i + 1)
        es[i + 1].append(i)
    return es


def make_binary(n):  # 平衡二分木
    es = [[] for _ in range(n)]
    for i in range(1, n):
        es[i].append((i - 1) // 2)
        es[(i - 1) // 2].append(i)
    return es


def make_star(n):  # スターグラフ
    es = [[] for _ in range(n)]
    for i in range(1, n):
        es[0].append(i)
        es[i].append(0)
    return es


def make_complete(n):  # 完全グラフ
    es = [[] for _ in range(n)]
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            es[i].append(j)
            es[j].append(i)
    return es


def make_rand(n, m):  # 多重辺, 自己ループなしの連結グラフ
    es = make_line(n)
    connect = [{1}] + [{i - 1, i + 1} for i in range(1, n - 1)] + [{n - 1}]
    for i in range(m - n):
        a, b = randint(0, n - 1), randint(0, n - 1)
        if a != b and not a in connect[b]:
            es[a].append(b)
            es[b].append(a)
            connect[a].add(b)
            connect[b].add(a)
    return es


def make_circle(n):
    es = make_line(n)
    es[0].append(n - 1)
    es[n - 1].append(0)
    return es
