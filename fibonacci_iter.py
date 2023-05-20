import time

start_time = time.time()


def fib(n: int) -> int:
    if n == 0:
        return 0
    last: int = 0
    next: int = 1

    for _ in range(1, n):
        last, next = next, next + last
    return next


if __name__ == '__main__':
    fib(30)
    print("--- %s seconds ---" % (time.time() - start_time))
