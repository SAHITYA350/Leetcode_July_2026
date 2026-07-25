class Solution:
    def maxProduct(self, n: int) -> int:

        digits = []

        while n:
            digits.append(n % 10)
            n //= 10

        ans = 0

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):

                # Try every pair.
                ans = max(ans, digits[i] * digits[j])

        return ans