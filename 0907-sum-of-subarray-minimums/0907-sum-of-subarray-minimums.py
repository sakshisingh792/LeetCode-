class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)

        pse = [-1] * n
        nse = [n] * n

        stack = []

        # Previous Smaller Strictly
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            pse[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []

        # Next Smaller or Equal
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            nse[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0

        for i in range(n):
            left = i - pse[i]
            right = nse[i] - i

            ans += arr[i] * left * right

        return ans % MOD