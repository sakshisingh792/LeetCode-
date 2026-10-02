class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        
        int n=strs.length;
        String start=strs[0];
        String end=strs[n-1];
        StringBuilder  sb=new StringBuilder();
        int min=Math.min(start.length(),end.length());
        for(int i=0;i<min;i++){
            if(start.charAt(i)== end.charAt(i)){
                sb.append(start.charAt(i));
            }
            else{
                return sb.toString();
            }
        }
        return sb.toString();

        
    }
}