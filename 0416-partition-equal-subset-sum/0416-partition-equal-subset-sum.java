class Solution {
    public boolean canPartition(int[] nums) {

        int sum = Arrays.stream(nums).sum();

        if (sum % 2 != 0) {
            return false;
        }

        int target = sum / 2;
        int n = nums.length;

        boolean[][] dp = new boolean[n][target + 1];

        // Sum 0 is possible using no elements
        for (int i = 0; i < n; i++) {
            dp[i][0] = true;
        }

        // Using only nums[0]
        if (nums[0] == target) {
            dp[0][nums[0]] = true;
        }

        // Fill the table
        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= target; j++) {

                boolean pick = false;

                if (nums[i] <= j) {
                    pick = dp[i - 1][j - nums[i]];
                }

                boolean notpick = dp[i - 1][j];

                dp[i][j] = pick || notpick;
            }
        }

        return dp[n - 1][target];
    }
}