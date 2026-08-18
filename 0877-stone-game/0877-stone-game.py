class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def solve(i, j):
            if i > j:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]

            left = piles[i] - solve(i + 1, j)
            right = piles[j] - solve(i, j - 1)

            dp[(i, j)] = max(left, right)

            return dp[(i, j)]

        return solve(0, len(piles) - 1) > 0