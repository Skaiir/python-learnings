from typing import List

def plusOne(digits: List[int]) -> List[int]:
    read_i = len(digits) - 1
    repeat = True
    while repeat and read_i >= 0:
        if digits[read_i] == 9:
            digits[read_i] = 0
            read_i -= 1
        else:
            digits[read_i] += 1
            repeat = False
    if repeat:
        digits = digits.insert(0, 1)
    return digits