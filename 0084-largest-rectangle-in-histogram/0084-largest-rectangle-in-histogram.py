class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        next_smal=[0]*n
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                next_smal[i]=n
            else:
                next_smal[i]=stack[-1]
            stack.append(i)     

        stack=[]
        prev_sm=[0]*n
        for i in range(n):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                prev_sm[i]=-1
            else:
                prev_sm[i]=stack[-1] 
            stack.append(i)    
        area=0
        max_area=float("-inf")
        for i in range(n):
            l=heights[i]
            b=next_smal[i]-prev_sm[i]-1
            area=l*b
            max_area=max(area,max_area)   

        return max_area                             


        