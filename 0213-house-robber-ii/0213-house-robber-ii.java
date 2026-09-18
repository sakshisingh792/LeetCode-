class Solution {
    public int rob(int[] nums) {
        int n=nums.length;
        if (n==1){
            return nums[0];
        }
        int first=solve(nums,0,n-2);
        int last=solve(nums,1,n-1);
        return Math.max(first,last);
        
    }
    public int solve(int[] nums, int start, int end){
        int[] dp=new int[end-start+1];
        dp[0]=nums[start];
        if(dp.length>1){
            dp[1]=Math.max(nums[start],nums[start+1]);
        }
        for(int i=2;i<dp.length;i+=1){
            int rob=nums[start+i]+dp[i-2];
            int notrob=dp[i-1];
            dp[i]=Math.max(rob,notrob);
        }
        return dp[dp.length-1];
    }
}