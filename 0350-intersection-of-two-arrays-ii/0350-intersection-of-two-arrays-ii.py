class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1={}
        for num in nums1:
            freq1[num]=freq1.get(num,0)+1


        freq2={}
        for num in nums2:
            freq2[num]=freq2.get(num,0)+1

        ans=[]
        for i in freq1:
            if i in freq2 :
                if freq1[i]>freq2[i]:
                    for j in range(freq2[i]):
                        ans.append(i)
                else:
                    for j in range(freq1[i]):
                        ans.append(i)
        return ans                



        