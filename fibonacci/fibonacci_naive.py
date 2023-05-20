import time

start_time = time.time()


def fib(n: int):
    return n if n < 2 else fib(n-2) + fib(n-1)


print(fib(0))
print("--- %s seconds ---" % (time.time() - start_time))
