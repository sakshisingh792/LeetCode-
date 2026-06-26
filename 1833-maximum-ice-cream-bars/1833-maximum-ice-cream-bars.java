class Solution {
    public int maxIceCream(int[] costs, int coins) {
        Arrays.sort(costs);
        int count=0;
        int n= costs.length;
        int sum=0;
        for (int i=0;i<n;i++){
            sum+=costs[i];
            if (sum>coins){
                break;
            }
            count+=1;
        }
        return count;
        
    }
}