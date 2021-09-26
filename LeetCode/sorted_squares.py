def sortedSquares(nums: int) -> int:
    
    # find the point where 0 crosses over
    # have two pointer travel up and down from that point, inserting based on abs([x])

    arr_len = len(nums)
    
    first_positive = 0
    
    while first_positive < arr_len:
        if nums[first_positive] >= 0:
            break
        first_positive += 1
    
    if first_positive == 0:
        return [num ** 2 for num in nums]
    elif first_positive == arr_len or (first_positive == arr_len - 1 and nums[first_positive] == 0):
        return [num ** 2 for num in nums][::-1]
    
    else:
        out_arr = []
        climber_p = first_positive
        descender_p = first_positive - 1
        
        while climber_p < arr_len and descender_p >= 0:
            climber_num = nums[climber_p]                
            descender_num = nums[descender_p]                
            if climber_num <= abs(descender_num):
                out_arr.append(climber_num ** 2)
                climber_p += 1
            else:
                out_arr.append(descender_num ** 2)
                descender_p -= 1
        
        while climber_p < arr_len:
            out_arr.append(nums[climber_p] ** 2)
            climber_p += 1

        while descender_p >= 0:
            out_arr.append(nums[descender_p] ** 2)
            descender_p -= 1
            
        return out_arr

print(sortedSquares([-3, -1, 0, 1, 7, 12]))