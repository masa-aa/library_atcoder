def compress(arr):
    return list(map({e: i for i, e in enumerate(sorted(set(arr)))}.__getitem__, arr))
