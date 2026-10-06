class Solution {

    public boolean wordBreak(String s, List<String> wordDict) {

        HashSet<String> set = new HashSet<>(wordDict);

        int n = s.length();

        Boolean[] dp = new Boolean[n];

        return solve(s, set, 0, n, dp);
    }

    public boolean solve(String s, HashSet<String> set, int i, int n, Boolean[] dp) {

        if (i == n) {
            return true;
        }

        // Already calculated
        if (dp[i] != null) {
            return dp[i];
        }

        for (int j = i; j < n; j++) {

            String ch = s.substring(i, j + 1);

            if (set.contains(ch) && solve(s, set, j + 1, n, dp)) {
                dp[i] = true;
                return true;
            }
        }

        dp[i] = false;
        return false;
    }
}