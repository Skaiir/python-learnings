from typing import List

def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:
    max_sum = k * threshold
    curr_sum = sum(arr[:k])
    offset = 0
    count = 1 if curr_sum <= max_sum else 0
    for offset in range(len(arr) - k):
        curr_sum -= arr[offset]
        curr_sum += arr[offset+k]
        if curr_sum <= max_sum:
            count += 1
    return count

numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4)