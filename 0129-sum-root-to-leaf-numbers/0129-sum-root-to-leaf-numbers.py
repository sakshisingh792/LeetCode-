# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def sumNumbers(self, root: Optional[TreeNode]) -> int:
            ans=[]
            def dfs(node,path):
                if node==None:
                    return

                path.append(node.val)    

                if not node.right and not node.left:
                    ans.append("".join(map(str,path)))




                dfs(node.left,path)
                dfs(node.right,path)  
                path.pop()  
            
            dfs(root,[])
            res=0
            for ch in ans:
                res+=int(ch)
            return res   
