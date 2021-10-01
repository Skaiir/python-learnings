import timeit

def combine(n: int, k: int):
    # nums n, n-1, ... 2 , 1
    initial_nums = list(range(1, n + 1))[::-1]
    def combine_recurse(k, nums):
        n = len(nums)
        range_list = list(range(0, n-k+1))
        for x in range_list:
            if k == 1:
                yield [nums[x]]
            else:
                for result in combine_recurse(k-1, nums[x+1:]):
                    yield [nums[x]] + result
    return list(combine_recurse(k, initial_nums))


# print(timeit.timeit("combine(2, 1)", setup="from __main__ import combine", number= 1) * 1000)
# print(timeit.timeit("combine(4, 2)", setup="from __main__ import combine", number= 1) * 1000)
# print(timeit.timeit("combine(8, 4)", setup="from __main__ import combine", number= 1) * 1000)
# print(timeit.timeit("combine(12, 5)", setup="from __main__ import combine", number= 1) * 1000)
# print(timeit.timeit("combine(16, 5)", setup="from __main__ import combine", number= 1) * 1000)
# print(timeit.timeit("combine(20, 5)", setup="from __main__ import combine", number= 1) * 1000)
# print(timeit.timeit("combine(40, 5)", setup="from __main__ import combine", number= 1) * 1000)

f = open("output.txt", mode="w+")
f.write(str(combine(20, 5)))
f.close()