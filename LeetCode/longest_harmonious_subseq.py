from typing import Sequence


def findLHS(nums):
    nums.sort()
    even_up = [(x + 1 if not x&1 else x) for x in nums]
    even_down = [(x - 1 if not x&1 else x) for x in nums]
    iter_arr = even_up + [10 ** 10] + even_down
    last_val = 10 ** 10
    count_max = 0
    count_curr = 0
    for x in iter_arr:
        if x == last_val:
            count_curr += 1
        else:
            count_curr = 1
        count_max = max(count_max, count_curr)
        last_val = x
    return count_max

# this doesn't work for 1,1,1,1

def findLHS2(nums):
    nums.sort()
    diff_arr = [nums[x + 1] - nums[x] for x in range(len(nums) - 1)]
    longest_seq = 0
    
    for i, val in enumerate(diff_arr):
        if val == 1:
            current_seq = 2
            sub_i = i
            while sub_i - 1 >= 0 and diff_arr[sub_i - 1] == 0:
                sub_i -= 1
                current_seq += 1
            sub_i = i
            while sub_i + 1 < len(diff_arr) and diff_arr[sub_i + 1] == 0:
                sub_i += 1
                current_seq += 1
            longest_seq = max(longest_seq, current_seq)

    return longest_seq



findLHS2([1,2,2,1])