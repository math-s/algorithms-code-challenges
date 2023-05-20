from test_sorted_array import test_if_array_is_sorted
import time
from typing import Dict

A = [
    58, 41, 81, 14, 17, 98, 93, 1, 22, 20, 39, 76, 98, 57, 77, 64, 44, 4, 32, 67, 72, 99, 54, 24, 92, 2, 19, 55, 75, 34, 56, 48, 83, 88, 88, 87, 29, 35, 12, 60, 68, 9, 60, 89, 99, 88, 48, 32, 84,
    20, 13, 4, 71, 82, 30, 8, 24, 46, 47, 36, 58, 10, 26, 45, 74, 1, 57, 9, 21, 3, 31, 51, 86, 6, 94, 61, 5, 48, 89, 36, 58, 4, 56, 60, 31, 47, 77, 15, 98, 33, 54, 90, 92, 80, 16, 27, 3, 48, 74, 95
]
B = [
    58, 41, 81, 14, 17, 98, 93, 1, 22, 20, 39, 76, 98, 57, 77, 64, 44, 4, 32, 67, 72, 99, 54, 24, 92, 2, 19, 55, 75, 34, 56, 48, 83, 88, 88, 87, 29, 35, 12, 60, 68, 9, 60, 89, 99, 88, 48, 32, 84,
    20, 13, 4, 71, 82, 30, 8, 24, 46, 47, 36, 58, 10, 26, 45, 74, 1, 57, 9, 21, 3, 31, 51, 86, 6, 94, 61, 5, 48, 89, 36, 58, 4, 56, 60, 31, 47, 77, 15, 98, 33, 54, 90, 92, 80, 16, 27, 3, 48, 74, 95
]


def sort_array(array: list) -> list:
    for j in range(len(array)):
        value = array[j]
        i = j - 1
        while i >= 0 and array[i] > value:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = value


my_start_time = time.time()
sort_array(A)
print("--- %s seconds ---" % (time.time() - my_start_time))

python_start_time = time.time()
B.sort()
print("--- %s seconds ---" % (time.time() - python_start_time))

test_if_array_is_sorted(A)
test_if_array_is_sorted(B)
