class Solution {
    public String getHint(String secret, String guess) {

        int bulls = 0;
        int cows = 0;

        int[] secretCount = new int[10];
        int[] guessCount = new int[10];

        // Step 1: Find bulls
        // Also count non-bull digits
        for(int i = 0; i < secret.length(); i++) {

            if(secret.charAt(i) == guess.charAt(i)) {
                bulls++;
            }
            else {
                secretCount[secret.charAt(i) - '0']++;
                guessCount[guess.charAt(i) - '0']++;
            }
        }

        // Step 2: Find cows
        for(int digit = 0; digit < 10; digit++) {
            cows += Math.min(secretCount[digit], guessCount[digit]);
        }

        return bulls + "A" + cows + "B";
    }
}