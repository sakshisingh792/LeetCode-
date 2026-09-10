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
    int ans=0;
    public int averageOfSubtree(TreeNode root) {
        
        traverse(root);
        return ans;


        
        
    }
    public int sum(TreeNode node){
        if (node == null){
            return 0;
        }

        return node.val+sum(node.left)+sum(node.right);

    }

    public int count(TreeNode node){
        if(node ==null){
            return 0;
        }
        return 1+ count(node.left)+count(node.right);
    }
    public void traverse(TreeNode node){
        if (node ==null){
            return;
        }
        int totsum=sum(node);
        int totcon=count(node);
        if((totsum/totcon==node.val)){
            ans++;
        }
        traverse(node.left);
        traverse(node.right);
    }
}