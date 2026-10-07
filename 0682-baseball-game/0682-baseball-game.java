class Solution {
    public int calPoints(String[] s) {

        ArrayList<Integer> arr = new ArrayList<>();

        for (int i = 0; i < s.length; i++) {

            if (s[i].equals("C")) {
                arr.remove(arr.size() - 1);
            }

            else if (s[i].equals("D")) {
                int last = arr.get(arr.size() - 1);
                arr.add(2 * last);
            }

            else if (s[i].equals("+")) {
                int last = arr.get(arr.size() - 1);
                int secondLast = arr.get(arr.size() - 2);

                arr.add(last + secondLast);
            }

            else {
                arr.add(Integer.parseInt(s[i]));
            }
        }

        int sum = 0;

        for (int score : arr) {
            sum += score;
        }

        return sum;
    }
}