import sys
from numpy import random

try:
    length = int(sys.argv[1])
except IndexError:
    length = 10

try:
    limit_botton = int(sys.argv[2])
except IndexError:
    limit_botton = 0

try:
    limit_up = int(sys.argv[3])
except IndexError:
    limit_up = 10


result = random.randint(limit_botton, limit_up, length)

str_result = "[" + ",".join(map(str, result)) + "]"
print(str_result)
