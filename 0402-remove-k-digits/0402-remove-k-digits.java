class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Character> st = new Stack<>();

        for (int i = 0; i < num.length(); i++) {

            while (!st.isEmpty() && st.peek() > num.charAt(i) && k > 0) {
                st.pop();
                k--;
            }

            st.push(num.charAt(i));
        }

        // If k digits are still remaining, remove from the end
        while (!st.isEmpty() && k > 0) {
            st.pop();
            k--;
        }

        if (st.isEmpty()) {
            return "0";
        }

        // Build answer
        StringBuilder sb = new StringBuilder();

        while (!st.isEmpty()) {
            sb.append(st.pop());
        }

        // Stack was popped from right to left
        sb.reverse();

        // Remove leading zeros
        int i = 0;
        while (i < sb.length() && sb.charAt(i) == '0') {
            i++;
        }

        if (i == sb.length()) {
            return "0";
        }

        return sb.substring(i);
    }
}