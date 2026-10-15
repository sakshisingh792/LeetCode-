class Solution {
    public long countSubarrays(int[] nums, int k) {
        int maxm=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]>maxm){
                maxm=nums[i];
            }
        }
        int left=0;
        int count=0;
        long ans=0;
        for(int right=0;right<nums.length;right++){
            if(nums[right]==maxm){
                count++;

            }
            while(count>=k){
                if(nums[left]==maxm){
                    count--;
                }
                left++;
            }
            ans+=left;

        }
        return ans;
        
    }
}