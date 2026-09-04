class Solution:

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.check(root, subRoot)

    def check(self, root, subRoot):
        if root is None:
            return False

        if self.is_same(root, subRoot):
            return True

        return (self.check(root.left, subRoot) or
                self.check(root.right, subRoot))


    def is_same(self, root1, root2):
        if root1 is None and root2 is None:
            return True

        if root1 is None or root2 is None:
            return False

        if root1.val != root2.val:
            return False

        return (self.is_same(root1.left, root2.left) and
                self.is_same(root1.right, root2.right))