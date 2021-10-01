import timeit


def containsDuplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            num_set.add(num)
        return True
    return False

def containsDuplicate2(nums):
    return (len(nums) > len(set(nums)))

count = 1000

dupe_arr = list(range(count))
no_dupe_arr = list(range(count))
dupe_arr[int(count / 2 + 1)] = 1

print(timeit.timeit('containsDuplicate(dupe_arr)', setup='from __main__ import containsDuplicate, dupe_arr', number=100000))
print(timeit.timeit('containsDuplicate2(dupe_arr)', setup='from __main__ import containsDuplicate2, dupe_arr', number=100000))