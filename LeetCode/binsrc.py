from typing import List

def search( nums: List[int], target: int) -> int:
    lo_i = 0
    hi_i = len(nums) - 1
    while lo_i <= hi_i:
        i = (lo_i + hi_i) // 2
        num_i = nums[i]
        if num_i == target:
           return i
        elif num_i < target:
            lo_i = i + 1
        else:
            hi_i = i - 1
    return -1

search([-1,0,3,5,9,12], 2)
