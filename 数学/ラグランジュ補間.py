def lagrange_interpolation(xk_yk: list, x: int, mod: int = 1000000007):
    """n次関数f(x)の値 y_k = f(x_k)が n + 1 個与えられて, 
       ラグランジュ補間によってf(x)の値を求める．O(n^2)
    """
    px = 0
    for i, (xs, ys) in enumerate(xk_yk):
        fi = 1
        for j, (xt, _) in enumerate(xk_yk):
            if i != j:
                ys = ys * (x - xt) % mod
                fi = fi * (xs - xt) % mod
        ys *= pow(fi, mod - 2, mod)
        px += ys % mod
    return px % mod

# https://atcoder.jp/contests/arc033/tasks/arc033_4 80点
