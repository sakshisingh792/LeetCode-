class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr)<=1:
                return arr
            mid=len(arr)//2
            left=merge_sort(arr[:mid])
            right=merge_sort(arr[mid:])
            return merge(left,right)

        def merge(left,right):
            i=0
            j=0
            ans=[]
            while i<len(left) and j<len(right) :
                if left[i]<right[j]:
                    ans.append(left[i])
                    i+=1
                else:
                    ans.append(right[j])
                    j+=1

            while i<len(left):
                ans.append(left[i])
                i+=1

            while j<len(right):
                ans.append(right[j])
                j+=1  

            return ans    
        return merge_sort(nums)
                                


