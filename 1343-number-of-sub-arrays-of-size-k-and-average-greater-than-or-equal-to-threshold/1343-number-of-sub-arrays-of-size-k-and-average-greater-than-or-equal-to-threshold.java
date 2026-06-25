class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int ans=0;
        int left=0;
        int n=arr.length;
        int cur_sum=0;
        for(int right=0;right<n;right++){
            cur_sum+=arr[right];
            if (right-left+1>k){
                cur_sum-=arr[left];
                left++;
            }
            if (right-left+1==k){
                if (cur_sum>=threshold*k){
                    ans++;

                }
            }
        }
        return ans;
        
    }
}