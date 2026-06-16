class Solution:
    def shortestSubarray(self, nums: List[int], k: int):
        n = len(nums)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        q = deque()
        ans = float("inf")

        for i in range(n + 1):

            while q and prefix[i] - prefix[q[0]] >= k:
                ans = min(ans, i - q.popleft())

            while q and prefix[q[-1]] >= prefix[i]:
                q.pop()

            q.append(i)

        return ans if ans != float("inf") else -1