class Solution {
    public boolean canPartition(int[] nums) {
        int  sum=0;
        for(int num: nums){
            sum+=num;
        }
        if(sum%2!=0){
            return false;
        }
        int n =nums.length; 
        int target=sum/2;
        boolean[][] dp=new boolean[n][target+1];
        for(int i =0;i<n;i++){
            dp[i][0]=true;
        }
        if(nums[0]<=target){
            dp[0][nums[0]]=true;
        }

        for(int i=1;i<n;i++){
            for(int j=1;j<=target;j++){
                if(nums[i]<=j){
                    dp[i][j]=dp[i-1][j-nums[i]]|| dp[i-1][j];
                }
                else{
                    dp[i][j]=dp[i-1][j];
                }
            }
        }
        return dp[n-1][target];


    }}

      