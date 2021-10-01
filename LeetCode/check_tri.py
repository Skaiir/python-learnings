def largestPerimeter2(nums):
    nums.sort()
    for x in range(-3, -len(nums) - 1, -1):
        if nums[x] <= nums[-1] - nums[-2]:
            return nums[x] + sum(nums[-2:])
    return 0

def largestPerimeter(nums):
    nums.sort(reverse = True)
    for l_s in range(0, len(nums) - 2):
        for m_s in range(l_s + 1, len(nums) - 1):
            if nums[m_s] < nums[l_s] / 2:
                break
            if nums[m_s] + nums[m_s + 1] > nums[l_s]:
                return nums[m_s] + nums[m_s + 1] + nums[l_s]
    return 0

largestPerimeter([1,2,1])
largestPerimeter([2,2,1])