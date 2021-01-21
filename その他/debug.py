def debug(*a):
    """I am print debugger"""
    def get_var_name(var):
        for k, v in globals().items():
            if id(v) == id(var):
                name = k
        return name
    print("-" * 50)
    if isinstance(a[0], list) and isinstance(a[0][0], list):
        b = a[0]
        name = get_var_name(b)
        s = "\n" + " " * (len(name) + 4)
        mat = s.join(" ".join(map(str, v)) for v in b)
        print(" {} = {}".format(name, mat))
    else:
        if isinstance(a[0], list or tuple):
            a = a[0]
            print(" {} = {}".format(get_var_name(a), a))
        else:
            for val in iter(a):
                print(" {} = {}".format(get_var_name(val), val))
    print("-" * 50)



if __name__ == '__main__':
    a = 1
    b = 2
    c = 3
    debug(a, b, c)
    """
    ------------------------------
     a = 1
     b = 2
     c = 3
    ------------------------------
    """
    dp = [1, 2, 3, 4, 5]
    debug(dp)
    """
    ------------------------------
     dp = [1, 2, 3, 4, 5]
    ------------------------------
    """
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    debug(matrix)
    """
    ------------------------------
     matrix = 1 2 3
              4 5 6
              7 8 9
    ------------------------------
    """
