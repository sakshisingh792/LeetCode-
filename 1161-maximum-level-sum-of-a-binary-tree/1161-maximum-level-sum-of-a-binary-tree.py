# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        if root ==None:
            return []

        q=deque([root])
        maxm=float("-inf")
        res=1
        level_num=0
        while q:
            n=len(q)
            level_sum=0
            level_num+=1
            
            for _ in range(n):
                node=q.popleft()
                level_sum+=node.val


                if node.left:
                    q.append(node.left)
                if node.right :
                    q.append(node.right )
            if level_sum>maxm:
                maxm=level_sum
                res=level_num
        return res        


        