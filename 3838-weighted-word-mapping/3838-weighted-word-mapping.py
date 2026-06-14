class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=""

        for word in words:
            summ=0
            for let in word:
                idx=ord(let)-ord("a")
                summ+=weights[idx]
            idnx=summ%26
            
            ans +=chr(ord('z') - idnx)
        return ans        



        