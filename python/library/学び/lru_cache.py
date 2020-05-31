# フィボナッチ数列のメモ化再帰をLRU_cacheを使ってする
from functools import lru_cache
@lru_cache(None) # depth無限大
def fib(n):
    if n<2:return n
    return fib(n-1)+fib(n-2)
print(fib(4))