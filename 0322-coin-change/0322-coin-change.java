class Solution {
    public int coinChange(int[] coins, int amount) {
        int n = coins.length;
        int[][] dp=new int[n][amount+1];
        for(int[] rows:dp){
           Arrays.fill(rows,-1);
        }

        int ans = solve(n - 1, amount, coins,dp);

        return ans == Integer.MAX_VALUE ? -1 : ans;
    }

    public int solve(int index, int target, int[] arr,int[][] dp) {

        // Only coin arr[0] is available
        if (index == 0) {
            if (target % arr[0] == 0) {
                return target / arr[0];
            }
            return Integer.MAX_VALUE;
        }

        // Pick the current coin
        int pick = Integer.MAX_VALUE;
        if(dp[index][target]!=-1){
            return dp[index][target];
        }

        if (arr[index] <= target) {
            int result = solve(index, target - arr[index], arr,dp);

            if (result != Integer.MAX_VALUE) {
                pick = 1 + result;
            }
        }

        // Don't pick current coin
        int notpick = solve(index - 1, target, arr,dp);

        dp[index][target]= Math.min(pick, notpick);
        return dp[index][target];
    }
}