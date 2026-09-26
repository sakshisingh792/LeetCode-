class Solution {
    public int lengthOfLIS(int[] nums) {
        int n=nums.length;
        int[][] dp=new int[n][n];
        for(int[] row:dp){
            Arrays.fill(row,-1);

        }
        return solve(nums,0,-1,dp);


    }
    public int solve(int[] nums,int ind,int prev,int[][] dp){
        int n=nums.length;
        if(ind==n){
            return 0;
        }
        if(prev!=-1 && dp[ind][prev]!=-1 ){
            return dp[ind][prev];
        }

        int skip=solve(nums,ind+1,prev,dp);
        int pick=0;
        if(prev==-1 || nums[ind]>nums[prev]){
            pick=1+solve(nums,ind+1,ind,dp);
        }
        if(prev!=-1){
            dp[ind][prev]=Math.max(pick,skip);
        }
        return Math.max(pick,skip);
    }
}