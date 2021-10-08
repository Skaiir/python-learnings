from typing import List
# Ungodly slowness
def numOfSubarrays(arr: List[int]) -> int:
    count = len([i for i in arr if i&1])
    arr_base = arr.copy()
    arlen = len(arr)
    for x in range(1, arlen):
        for y in range(x, arlen):
            arr[y] = arr[y] + arr_base[y-x]
            if arr[y]&1:
                count +=1
    return count % (10**9 + 7)

numOfSubarrays([1,3,5])