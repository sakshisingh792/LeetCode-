class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        n=len(apple)
        m=len(capacity)
        total=sum(apple)
        boxes=0
        capacity.sort(reverse=True)
        tot_cap=0
        for i in range(m):
            if tot_cap<total :
                boxes+=1
                tot_cap+=capacity[i]
            else:
                break    
        return boxes      
        