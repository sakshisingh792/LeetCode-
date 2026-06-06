# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        ans=[]
        q=deque([root])
        if root==None:
            return ans

        leftToRight=True
        while q:
            n=len(q)
            level=[0]*n
            for i in range(n):
                node=q.popleft()
                index=i if leftToRight else n-i-1  
                level[index]=node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            ans.append(level)
            leftToRight=not leftToRight  

        return ans              
        