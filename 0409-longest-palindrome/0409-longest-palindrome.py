class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq=Counter(s)
        odd_found=False
        total=0
        for count in freq.values():
            if count%2==0:
                total+=count 
            else:
                total+=count-1
                odd_found=True

        if odd_found:
            total+=1
        return total    


        