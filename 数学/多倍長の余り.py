# n%a を求める

n = list(map(int, input()))


def rem(n, a):
    ans = 0
    for i in n:
        ans *= 10
        ans += i
        ans %= a
    return ans


# print(rem(int(input())),n)
