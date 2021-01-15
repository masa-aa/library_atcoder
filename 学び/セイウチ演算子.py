# Python 3.8以降
def modlist(a, Len, mod):
    tmp = 1
    return [1] + [tmp := tmp * a % mod for i in range(Len - 1)]


if __name__ == '__main__':
    print(modlist(3, 5, 10))
