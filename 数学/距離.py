def d(x: list, y: list) -> float:
    """n=len(x)=len(y)してn次元ベクトルx, yのユークリッド距離"""
    return sum((i - j) * (i - j) for i, j in zip(x, y))**0.5


def d_k(x: list, y: list, k=2) -> float or int:
    """n=len(x)=len(y)してn次元ベクトルx, yのk乗距離"""
    if k == "inf":
        return max(abs(i - j) for i, j in zip(x, y))

    elif k == 1:
        return sum(abs(i - j) for i, j in zip(x, y))

    return sum((i - j)**k for i, j in zip(x, y))**(1 / k)
