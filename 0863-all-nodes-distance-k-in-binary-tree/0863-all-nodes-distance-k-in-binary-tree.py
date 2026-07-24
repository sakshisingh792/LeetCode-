# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        from collections import deque

        def parent_map(root):
            parent={}
            q=deque([root])

            while q:
                node=q.popleft()
                if node.left:
                    parent[node.left]=node
                    q.append(node.left)

                if node.right:
                    parent[node.right]=node
                    q.append(node.right)


            return parent

        def ans(parent):
            q=deque([target])
            visited=set([target])
            lvl_cnt=0

            while q  :
                n=len(q)
                if lvl_cnt==k:
                    return [node.val for node in q]
                for _ in range(n):
                    node=q.popleft()
                    if node.left and node.left not in visited:
                        visited.add(node.left)
                        q.append(node.left)


                    if node.right and node.right not in visited:
                        visited.add(node.right)
                        q.append(node.right)


                    if node in parent and parent[node] not in visited  :
                        visited.add(parent[node])  
                        q.append(parent[node])
                lvl_cnt+=1   
            return []
        if not root:
            return []

        parent=parent_map(root)
        return ans(parent)                                   
        