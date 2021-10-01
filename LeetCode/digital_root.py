from itertools import count
import random
import timeit

def addDigits(num: int) -> int:
    while num >= 10:
        num = sum(int(c) for c in str(num))
    return num

def addDigits2(num: int) -> int:
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9

print(timeit.timeit("addDigits(random.randint(0, 1000000))", setup="from __main__ import addDigits; import random", number=10000))
print(timeit.timeit("addDigits2(random.randint(0, 1000000))", setup="from __main__ import addDigits2; import random", number=10000))