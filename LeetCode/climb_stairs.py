import math
class Solution:
    def climbStairs(self, n: int) -> int:
        permutation_sum = 0
        two_count = 0
        while two_count * 2 <= n:
            a = math.factorial(n)
            b = math.factorial(n - two_count * 2)
            c = math.factorial(two_count * 2)
            permutation_sum += a / b / c
            two_count += 1
        return permutation_sum

sol = Solution()

print(sol.climbStairs(2))
print(sol.climbStairs(3))
print(sol.climbStairs(20))
print(sol.climbStairs(30))
print(sol.climbStairs(38))