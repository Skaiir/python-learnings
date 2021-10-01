import random
import timeit

def minimumAbsDifference1(arr):
    arr.sort()
    step_arr = [arr[x + 1] - arr[x] for x in range(len(arr) - 1)]
    min_step = min(step_arr)
    return [[arr[x], arr[x + 1]] for x in range(len(step_arr)) if step_arr[x] == min_step]

def minimumAbsDifference2(arr):
    arr.sort()
    mn = min(b - a for a, b in zip(arr, arr[1:]))
    return [[a, b] for a, b in zip(arr, arr[1:]) if b - a == mn]     

def minimumAbsDifference3(arr):
        arr.sort()
        minimum = float("inf")
        for i in range(len(arr) - 1):
            current = arr[i + 1] - arr[i]
            if current < minimum:
                minimum = current
        ans = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == minimum:
                ans.append([arr[i], arr[i + 1]])
        return ans

# input_data_ex = random.sample(range(-10**6, 10**6), random.randrange(2, 10**5))
input_data_ex = random.sample(range(-10**6, 10**6), 10000)

print(timeit.timeit('minimumAbsDifference1(input_data_ex)', setup='from __main__ import minimumAbsDifference1, input_data_ex', number=100))
print(timeit.timeit('minimumAbsDifference2(input_data_ex)', setup='from __main__ import minimumAbsDifference2, input_data_ex', number=100))
print(timeit.timeit('minimumAbsDifference3(input_data_ex)', setup='from __main__ import minimumAbsDifference3, input_data_ex', number=100))#

# 1.4990605
# 21.674769
# 3.1598903000000007