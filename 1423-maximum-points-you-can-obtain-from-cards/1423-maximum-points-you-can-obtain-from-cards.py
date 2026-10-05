class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n = len(nums)

        curr = sum(nums[:k])
        ans = curr

        left = 0

        for right in range(k):
            curr -= nums[k - 1 - right]
            curr += nums[n - 1 - right]

            ans = max(ans, curr)

        return ans