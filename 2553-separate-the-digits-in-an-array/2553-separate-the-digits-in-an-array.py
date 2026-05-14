class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer=[]
        for num in nums:
            val=str(num)
            for i in range(len(val)):
              answer.append(int(val[i]))
        return answer      