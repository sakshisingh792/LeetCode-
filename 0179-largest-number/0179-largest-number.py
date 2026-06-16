class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        nums=[str(num) for num in nums]

        def compare(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
        ans="".join(nums)
        if ans[0]=="0":
            return "0"
        else:
            return ans            
