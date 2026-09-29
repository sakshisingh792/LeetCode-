class Solution {
    public int minInsertions(String s) {
        int n=s.length();
        int[][] dp=new int[n][n];
        for(int[] row:dp){
            Arrays.fill(row,-1);
        }
        return solve(s,0,n-1,dp);
        
    }
    public int solve(String s , int start, int end,int[][] dp){
        if(start>=end){
            return 0;
        }
        if(dp[start][end]!=-1){
            return dp[start][end];
        }
        if(s.charAt(start)==s.charAt(end)){
            return solve(s,start+1,end-1,dp);
        }
        else{
            dp[start][end]= 1+Math.min(solve(s,start+1,end,dp),solve(s,start,end-1,dp));
        }
        return dp[start][end];
    }
}