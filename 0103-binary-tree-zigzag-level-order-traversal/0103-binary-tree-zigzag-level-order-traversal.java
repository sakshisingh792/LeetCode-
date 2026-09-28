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
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        Queue<TreeNode> q=new LinkedList<>();
        
       
        List<List<Integer>> ans=new ArrayList<>();
        if(root==null){
            return ans;
        }
         q.add(root);
        boolean rightToleft=true;
        while (!q.isEmpty()){
            int n=q.size();
            int[] arr=new int[n];
            for(int i=0;i<n;i++){
                TreeNode node=q.poll();
                if(!rightToleft){
                    arr[n-i-1]=node.val;
                    
                }
                else{
                    arr[i]=node.val;
                    
                }

                if(node.left!=null){
                    q.add(node.left);
                }
                if(node.right!=null){
                    q.add(node.right);
                }

            }
            List<Integer> level=new ArrayList<>();
            for(int x:arr){
                level.add(x);
            }
            ans.add(level);
            rightToleft=!rightToleft;

        }
        return ans;
        
    }
}