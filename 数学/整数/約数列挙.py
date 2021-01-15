def divisors(N):
    """Nの約数列挙"""
    divisors = []
    for i in range(1, N + 1):
        if i * i > N:
            break
        if N % i == 0:
            divisors.append(i)
            if N != i * i:
                divisors.append(N // i)

    return divisors


# 小さい順に欲しいとき
def sorted_divisors(N):
    lower_divisors, upper_divisors = [], []
    i = 1
    for i in range(1, N + 1):
        if i * i > N:
            break
        if N % i == 0:
            lower_divisors.append(i)
            if N != i * i:
                upper_divisors.append(N // i)
    return lower_divisors + upper_divisors[::-1]
