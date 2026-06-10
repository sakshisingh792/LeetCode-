class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        n = len(nums)

        window_sum = sum(nums[:k])
        max_summ = window_sum

        for right in range(k, n):
            window_sum += nums[right]
            window_sum -= nums[left]
            left += 1

            max_summ = max(window_sum, max_summ)

        return max_summ / k