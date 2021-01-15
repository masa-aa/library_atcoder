def create_array(*dims, initial=0):
    """初期値initialでdim[0]*dim[1]*...*dim[n]の配列を生成"""
    n = len(dims)
    # [[[... + [init] * m_0 + for _ in range(m_i)]...]...]...] の文字を生成
    code = "[" * n + "{}] * {}" + " for _ in range({})]" * (n - 1)
    # evalする
    # print(code.format(initial, *dims))
    return eval(code.format(initial, *reversed(dims)))


if __name__ == "__main__":

    a = create_array(2, 2, 3, initial=1)
    a[1][1][2] = 10
    print(a)
    # [[[1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 10]]]

    b = create_array(3, 2)
    print(b)
    # [[0, 0], [0, 0], [0, 0]]

    print(create_array(10))
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
