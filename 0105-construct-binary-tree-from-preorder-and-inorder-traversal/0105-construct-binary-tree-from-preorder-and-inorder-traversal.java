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
    int ind=0;
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        int n=preorder.length;
        return build(preorder,inorder,0,n-1);
        
        
    }
    public TreeNode build(int[] preorder,int[] inorder,int start,int end){
        if(start>end){
            return null;
        }

        TreeNode root=new TreeNode(preorder[ind]);
        ind++;
        int i=start;
        for(;i<end+1;i++){
            if(inorder[i]==root.val){
                break;
            }
        }
        root.left=build(preorder,inorder,start,i-1);
        root.right=build(preorder,inorder,i+1,end);

       return root;
        
    }
}