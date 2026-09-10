# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans=0
        def find_sum(node):
            if node is None:
                return 0

            return node.val +find_sum(node.left)+find_sum(node.right)  

        def count(node):
            if node is None:
                return 0
            return 1+count(node.left)+count(node.right)   

        def traverse(node):
            if node is None:
                return

            total_sum=find_sum(node)
            total_count=count(node)
            if (node.val==total_sum//total_count):
                self.ans+=1
            traverse(node.left)
            traverse(node.right) 
        traverse(root)
        return self.ans                      
        