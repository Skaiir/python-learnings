def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    # k size array solution, increment 1 by 1 and store the in betweens
    store = nums[-k:]
    for x in range(len(nums)):
        new_num = store[x % k]
        store[x % k] = nums[x]
        nums[x] = new_num

nums = [1,2,3,4,5,6]
rotate(nums, 3)
print(nums)