class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n=matrix.length;
        int m=matrix[0].length;
        int[][] dp=new int[n][m];
        for(int i=0;i<m;i++){
            dp[n-1][i]=matrix[n-1][i];
        }
        for(int i=n-2;i>=0;i--){
            for(int j=0;j<m;j++){
                int down=dp[i+1][j];
                int leftdia=Integer.MAX_VALUE;
                if(j>0){
                    leftdia=dp[i+1][j-1];
                }
                int rightdia=Integer.MAX_VALUE;
                if(j<n-1){
                    rightdia=dp[i+1][j+1];
                }
                dp[i][j]=matrix[i][j]+Math.min(down,Math.min(leftdia,rightdia));
            }

        }
        int ans=Integer.MAX_VALUE;
        for(int i=0;i<m;i++){
            if(dp[0][i]<ans){
                ans=dp[0][i];
            }
        }
        return ans;

        
    }
}