# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q=deque([(root,0)])
        ans=0
        while q:
            n=len(q)
            first=q[0][1]
            last=q[-1][1]

            for i in range(n):
                node,idx=q.popleft()

                if node.left:
                    q.append((node.left,idx*2))

                if node.right:
                    q.append((node.right,idx*2+1))
            ans=max(ans,last-first+1)
        return ans                
       