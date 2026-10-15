class Solution {
    public int[] beautifulArray(int n) {
        ArrayList<Integer> arr=new ArrayList<>();
        arr.add(1);
        while (arr.size()<n){
            ArrayList<Integer> ans=new ArrayList<>();
            for(int x : arr){
                if (2*x-1<=n){
                    ans.add(2*x-1);
                }
                
            }
            for(int x: arr){
                if(x*2<=n){
                    ans.add(x*2);
                }
            }
            arr=ans;
        }
        int[] res=new int[n];
        for(int i =0;i<n;i++){
            res[i]=arr.get(i);
        }
          return res;
        }
      
        
    }
