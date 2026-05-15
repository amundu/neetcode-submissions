class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        Stack<int[]> stack = new Stack();
        int[] output = new int[temperatures.length];
        for (int i = temperatures.length-1; i >= 0; i--){
            int curr = temperatures[i];
            while (!stack.empty() && stack.peek()[0] <= curr){
                stack.pop();
            }
            output[i] = stack.empty() ? 0 : stack.peek()[1] - i;
            stack.push(new int[]{curr, i});
        }
        return output;
    }
}
