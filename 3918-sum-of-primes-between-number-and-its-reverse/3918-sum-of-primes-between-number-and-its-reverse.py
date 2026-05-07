class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:

        # reverse the number
        rev = int(str(n)[::-1])

        start = min(n, rev)
        end = max(n, rev)

        def isPrime(num):

            if num <= 1:
                return False

            for i in range(2, num):

                if num % i == 0:
                    return False

            return True

        ans = 0

        for i in range(start, end + 1):

            if isPrime(i):
                ans += i

        return ans