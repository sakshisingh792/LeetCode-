/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        return check(root,subRoot);
        
    }

    public boolean check(TreeNode root1,TreeNode root2){
        if(root1==null){
            return false;
        }
        if(issame(root1,root2)){
            return true;
        }
        return check(root1.left,root2)|| check(root1.right,root2);



    }

    public boolean issame(TreeNode root1,TreeNode root2){
        if(root1==null && root2==null){
            return true;
        }
        if(root1==null|| root2==null){
            return false;
        }
        if(root1.val!=root2.val){
            return false;
        }
        return issame(root1.left,root2.left) && issame(root1.right,root2.right);
    }
}