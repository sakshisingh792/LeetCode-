class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map_sum={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in map_sum:
                return [map_sum[complement],i]
            else:
                map_sum[nums[i]]=i    
            


        