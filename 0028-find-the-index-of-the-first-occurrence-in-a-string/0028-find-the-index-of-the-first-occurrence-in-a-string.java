class Solution {
    public int strStr(String haystack, String needle) {
        int n =haystack.length();
        int m =needle.length();
        int i=0;
        StringBuilder sb=new StringBuilder(haystack);
        while(i<n-m+1){
            if((sb.substring(i,i+m).equals(needle))){
                return i;
            }
            i++;
        }
        return -1;
        
    }
}