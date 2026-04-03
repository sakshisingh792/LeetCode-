class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        i,j=0,n-1
        max_area=float("-inf")

        while i<n and j>0:
            breadth=j-i
            heights=min(height[i],height[j])
            area=breadth*heights
            max_area=max(max_area,area)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_area            

        