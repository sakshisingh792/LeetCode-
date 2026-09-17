class Solution {
    public int minSumOfLengths(int[] arr, int target) {
        int n=arr.length;
        int[] best=new int[n];
        Arrays.fill(best,Integer.MAX_VALUE);
        int currsum=0;
        int left=0;
        int ans=Integer.MAX_VALUE;
        int min_length=Integer.MAX_VALUE;
        int length=0;
        for (int right=0;right<n;right++){
            currsum+=arr[right];
            while (currsum>target){
                currsum-=arr[left];
                left+=1;

            }
            if(currsum==target){
                length=right-left+1;
                if(left>0 && best[left-1]!=Integer.MAX_VALUE){
                    ans=Math.min(ans,length+best[left-1]);
                }
                min_length=Math.min(length,min_length);
            }
            best[right]=min_length;
        }
        return ans==Integer.MAX_VALUE?-1:ans;


        
    }
}