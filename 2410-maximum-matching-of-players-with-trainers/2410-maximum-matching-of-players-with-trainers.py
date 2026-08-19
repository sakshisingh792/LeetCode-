class Solution:
    def matchPlayersAndTrainers(self, num1: List[int], num2: List[int]) -> int:
        num1.sort()
        num2.sort()
        i = 0
        j = 0
        count = 0

        while i < len(num1) and j < len(num2):

            if num1[i] <= num2[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return count