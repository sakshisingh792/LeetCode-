class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n=len(reward1)
        total=sum(reward2)
        diff=[]
        for i in range(n):
            diff.append(reward1[i]-reward2[i])

        diff.sort(reverse=True)
        for i in range(k):
            total+=diff[i]

        return total