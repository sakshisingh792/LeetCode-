class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans=new ArrayList<>();
        return solve(n,ans,"",0,0);
        
    }
    public List<String> solve(int n,List<String> ans, String s,int open,int close){
        if(s.length()==2*n){
            ans.add(s);
            return ans;
        }
        if(open<n){
            solve(n,ans,s+"(",open+1,close);
        }
        if(open>close){
            solve(n,ans,s+")",open,close+1);
        }
        return ans;
    }
}