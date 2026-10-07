class MinStack {
    ArrayList<Integer> st=new ArrayList<>(); 

    public MinStack() {
        st=new ArrayList<>();
       
        
    }
    
    public void push(int value) {
        st.add(value);
        
        
    }
    
    public void pop() {
        int n =st.size();
        st.remove(n-1);
       
        
    }
    
    public int top() {
        int n =st.size();
        return st.get(n-1);
        
    }
    
    public int getMin() {
        int min=st.get(0);
        for(int i=1;i<st.size();i++){
            if(st.get(i)<min){
                min=st.get(i);
            }
        }
        return min;
        
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(value);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */