class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF

        # Maximum positive 32-bit integer
        MAX_INT = 0x7FFFFFFF

        while b!=0:
            no_carry=a^b

            carry=(a&b)<<1

            a=no_carry & MASK

            b=carry & MASK

        if a <=MAX_INT:
            return a
        else:
            return  ~(a^MASK)        
        