class Solution {
    public int largestRectangleArea(int[] heights) {
        Stack<int[]> stack = new Stack();
        int maxArea = 0;
        for (int i = 0; i < heights.length; i++){
            int curr = heights[i];
            int prevPos = i;
            while (!stack.empty() && stack.peek()[0] >= curr){
                int[] val = stack.pop();
                prevPos = val[1];
                int area = val[0]* (i-val[1]);
                maxArea = Math.max(maxArea, area);
            }

            stack.push(new int[]{curr, prevPos});
        }
        while (!stack.empty()){
            int[] val = stack.pop();
            int area = val[0] * (heights.length-val[1]);
            maxArea = Math.max(maxArea, area);
        }
        return maxArea;
    }
}
