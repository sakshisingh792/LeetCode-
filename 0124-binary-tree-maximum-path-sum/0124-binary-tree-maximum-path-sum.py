# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxm=float("-inf")
        def solve(root):
            nonlocal maxm
            if root==None:
                return 0


            left=solve(root.left) 
            right=solve(root.right)

            got=left+right+root.val

            one=max(left,right) +root.val

            only=root.val

            maxm=max(maxm,got,only,one)
            return max( one,only)
        solve(root)
        return maxm        
        