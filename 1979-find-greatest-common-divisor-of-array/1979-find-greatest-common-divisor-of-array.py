class Solution:
    def findGCD(self, nums: List[int]) -> int:
        import math
        smal=min(nums)
        lar=max(nums)
        gcd=math.gcd(smal,lar)
        return gcd