class Solution {
    public boolean isMatch(String s, String p) {
        int n =s.length();
        int m=p.length();
        Boolean[][] dp=new Boolean[n][m];
        return solve(n-1,m-1,s,p,dp);
        
    }
    public boolean solve(int i,int j ,String s, String p,Boolean[][] dp){
        if(i<0 && j<0){
            return true;
        }
        if(j<0 && i>=0){
            return false;
        }
        if( i<0 && j>=0 ){
            for(int jj=0;jj<=j;jj++){
                if(p.charAt(jj)!='*'){
                    return false;
                }
            }
            return true;
        }
        if(dp[i][j]!=null){
            return dp[i][j];
        }

        if(s.charAt(i)==p.charAt(j) || p.charAt(j)=='?'){
            dp[i][j]= solve(i-1,j-1,s,p,dp);
        }
        else if(p.charAt(j)=='*'){
            dp[i][j]=solve(i-1,j,s,p,dp)|| solve(i,j-1,s,p,dp);
        }
        else{
        dp[i][j]= false;
        }

        return dp[i][j];
    }
}