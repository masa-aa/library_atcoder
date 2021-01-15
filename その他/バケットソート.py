def bucket_sort(a: list):
    """a[i] < len(a) である配列のソート"""
    counter = [0] * len(a)
    for i in a:
        counter[i] += 1
    res = [i for i, e in enumerate(counter) for _ in range(e)]
    return res


if __name__ == "__main__":
    a = [0, 0, 1, 4, 2, 1, 1, 4, 3, 2, 1]
    print(bucket_sort(a))
    print(sorted(a))
