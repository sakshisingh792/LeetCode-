class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        pair = {}
        ans = float("inf")

        for i, num in enumerate(nums):
            if num in pair:
                ans = min(ans, i - pair[num])

            n = num
            rev = 0
            while n > 0:
                rev = rev * 10 + n % 10
                n //= 10

            pair[rev] = i

        return -1 if ans == float("inf") else ans