def get_basis(a):
    """
    F_2 ^60の掃き出し法
    0<a[i]<=2^60(>10^18)が与えられてbasisの和で表せなければ追加してbasisを返す
    """
    basis = []
    for e in a:
        for b in basis:
            e = min(e, e ^ b)
        if e:
            basis.append(e)
    return basis


a = list(map(int, input().split()))
print(get_basis(a))
# 1 2 3 4 -> 1 2 4
