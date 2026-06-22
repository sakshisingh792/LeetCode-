class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        from collections import deque
        q=deque([root])
        if root==None:
            return 0
        
        count=0
        while q:
            n=len(q)
            for i in range(n):
                node=q.popleft()
                count+=1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return count                


