import time
from typing import Dict

start_time = time.time()

memo: Dict[int, int] = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]


if __name__ == '__main__':
    fib(30)
    print("--- %s seconds ---" % (time.time() - start_time))
