from math import sqrt


def Eratosthenes(n):
    """n未満の素数列挙 """
    if n < 4:
        return [] if n <= 2 else [2]
    n, correction = n - n % 6 + 6, 2 - (n % 6 > 1)
    sieve = [True] * (n // 3)
    for i in range(1, int(sqrt(n)) // 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k // 3::2 * k] = [False] * ((n // 6 - k * k // 6 - 1) // k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) // 3::2 * k] = [False] * \
                ((n // 6 - k * (k - 2 * (i & 1) + 4) // 6 - 1) // k + 1)

    return [2, 3] + [3 * i + 1 | 1 for i in range(1, n // 3 - correction) if sieve[i]]

    # # x が素数か判定したいとき
    # is_prime = [False] * n
    # is_prime[2] = True
    # is_prime[3] = True
    # for i in range(1, n // 3 - correction):
    #     if sieve[i]:
    #         is_prime[3 * i + 1 | 1] = True
    # return is_prime


# sieve = Eratosthenes(10**7)
# print(sieve)
