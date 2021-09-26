from typing import List

def searchInsert(nums: List[int], target: int) -> int:        
    
    lilen = len(nums) 
    hi_i = lilen - 1
    if nums[hi_i] < target:
        return lilen
    lo_i = 0
    
    while True:

        i = (lo_i + hi_i) // 2
        num_i = nums[i]    
        if num_i == target:
            return i
        elif num_i > target:
            hi_i = i
        else:
            lo_i = i

        if hi_i - lo_i < 2:
            if nums[lo_i] > target:
                return lo_i
            if nums[hi_i] < target:
                return hi_i + 1
            return hi_i

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
print(searchInsert([1,3,5,6], 0))
print(searchInsert([1], 0))