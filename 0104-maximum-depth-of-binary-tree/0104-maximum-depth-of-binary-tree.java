class Solution {
    public int maxDepth(TreeNode root) {
        return helper(root);
    }  // ← Missing closing brace here
    
    private int helper(TreeNode node){
        if (node == null){
            return 0;
        }
        int left = helper(node.left);
        int right = helper(node.right);
        return Math.max(left, right) + 1;
    }
}