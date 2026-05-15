class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;

    public MinStack() {
        this.stack = new Stack(); 
        this.minStack = new Stack(); 
    }
    
    public void push(int val) {
        stack.push(val);
        if (minStack.isEmpty()){
            minStack.push(0);
        }else{
            if (val < stack.get(minStack.peek())){
                minStack.push(stack.size()-1);
            }
        }
    }
    
    public void pop() {
        stack.pop();
        if (stack.size() == minStack.peek()){
            minStack.pop();
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return stack.get(minStack.peek());
    }
}
