class Solution {
    public int findTargetSumWays(int[] nums, int target) {
        return solve(nums, target, 0, 0);
    }
    
    private int solve(int[] nums, int target, int index, int currentSum) {
        // Base Case: All elements processed
        if (index == nums.length) {
            return currentSum == target ? 1 : 0;
        }
        
        // Choose: + before nums[index]
        int positive = solve(nums, target, index + 1, currentSum + nums[index]);
        
        // Choose: - before nums[index]
        int negative = solve(nums, target, index + 1, currentSum - nums[index]);
        
        // Count total valid paths from both branches
        return positive + negative;
    }
}