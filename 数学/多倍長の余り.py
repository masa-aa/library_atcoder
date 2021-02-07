def rem(n: list, a: int):
    """ n % a を求める"""
    ans = 0
    for i in n:
        ans *= 10
        ans += i
        ans %= a
    return ans
