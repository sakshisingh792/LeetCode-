class Solution {
    public int findLHS(int[] nums) {
        HashMap<Integer,Integer> freq= new HashMap<>();
        int ans=0;
        for (int num : nums){
            freq.put(num,freq.getOrDefault(num,0)+1);
            }

        for (int num:freq.keySet()){
            if(freq.containsKey(num+1)){
                ans=Math.max(ans,freq.get(num)+freq.get(num+1));
            }

        }  
        return ans;

        }
        
    }
