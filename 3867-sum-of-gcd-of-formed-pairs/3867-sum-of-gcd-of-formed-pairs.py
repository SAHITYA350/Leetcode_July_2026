from math import gcd
from typing import List

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_gcd = [0] * n

        maxi = 0

        for i in range(n):
            maxi = max(maxi, nums[i])
            prefix_gcd[i] = gcd(nums[i], maxi)

        prefix_gcd.sort()

        ans = 0
        l, r = 0, n - 1

        while l < r:
            ans += gcd(prefix_gcd[l], prefix_gcd[r])
            l += 1
            r -= 1

        return ans