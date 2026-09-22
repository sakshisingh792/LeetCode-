class Solution {
    public int change(int amount, int[] coins) {
        int n =coins.length;
        int[][] dp=new int[n][amount+1];
        for(int[] row:dp){
            Arrays.fill(row,-1);
        }
        return solve(0,amount,coins,dp);
        
    }
    public int solve(int i,int target,int[] arr,int[][] dp){
        int n=arr.length;
        if(target==0){
            return 1;
        }
        if(i==n){
            return 0;
        }
        if(dp[i][target]!=-1){
            return dp[i][target];

        }
        int pick=0;
        int notpick;
        if(arr[i]<=target){
            pick=solve(i,target-arr[i],arr,dp);
        }
        notpick=solve(i+1,target,arr,dp);

        dp[i][target]=pick+notpick;
        return dp[i][target];
    }
}