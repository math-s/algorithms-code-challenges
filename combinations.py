from functools import lru_cache
from math import factorial


@lru_cache
def factorial_cache(number):
    return factorial(number)


def combinate(n: int, p: int):
    return factorial_cache(n)/(factorial_cache(p)*factorial_cache(n-p))


if __name__ == '__main__':
    print(combinate(5, 2))
    print(combinate(6, 2))
    print(combinate(7, 2))
    print(combinate(8, 2))
    print(combinate(9, 2))
    print(combinate(10, 2))
    print(combinate(11, 2))
    print(combinate(12, 2))
    print(combinate(13, 2))
    print(combinate(14, 2))
    print(combinate(15, 2))
    print(combinate(16, 2))
    print(combinate(17, 2))
    print(combinate(18, 2))
