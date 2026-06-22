class Solution:
        def threeConsecutiveOdds(self, arr: List[int]) -> bool:

            for i in range(len(arr) - 2):
                flag = True

                for j in range(i, i + 3):
                    if arr[j] % 2 == 0:  # found an even number
                        flag = False
                        break

                if flag:
                    return True

            return False       

