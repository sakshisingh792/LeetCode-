class Solution:
    def solve(self, nums):
        n = len(nums)

        if n == 0:
            return 0

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            rob = nums[i] + dp[i-2]
            skip = dp[i-1]

            dp[i] = max(rob, skip)

        return dp[n-1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        ans = max(
            self.solve(nums[:n-1]),
            self.solve(nums[1:])
        )

        return ans