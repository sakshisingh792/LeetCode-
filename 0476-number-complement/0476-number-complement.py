class Solution:
    def findComplement(self, num: int) -> int:
        next=(1<<num.bit_length())-1
        return num ^ next
        