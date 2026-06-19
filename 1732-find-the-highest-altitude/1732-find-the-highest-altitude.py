class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest=0
        alt=0
        for i in range(len(gain)):
            alt+=gain[i]
            highest=max(highest,alt)
        return highest    
