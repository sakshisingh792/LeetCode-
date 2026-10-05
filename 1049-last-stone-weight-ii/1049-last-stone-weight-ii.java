class Solution {
    public int lastStoneWeightII(int[] nums) {
        int n = nums.length;

        int sum = 0;
        for (int num : nums) {
            sum += num;
        }

        boolean[][] dp = new boolean[n][sum + 1];

        for (int i = 0; i < n; i++) {
            dp[i][0] = true;
        }

        if (nums[0] <= sum) {
            dp[0][nums[0]] = true;
        }

        for (int i = 1; i < n; i++) {
            for (int j = 1; j <= sum; j++) {

                if (nums[i] <= j) {
                    dp[i][j] = dp[i - 1][j - nums[i]]
                             || dp[i - 1][j];
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        int ans = Integer.MAX_VALUE;

        for (int i = 0; i <= sum; i++) {
            if (dp[n - 1][i]) {
                int s2 = sum - i;
                int diff = Math.abs(i - s2);

                ans = Math.min(ans, diff);
            }
        }

        return ans;
    }
}