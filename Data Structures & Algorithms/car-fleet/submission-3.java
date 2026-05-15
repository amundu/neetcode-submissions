class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        double[][] zipped = new double[position.length][2];

        for (int i = 0; i < position.length; i++){
            zipped[i][0] = position[i];
            zipped[i][1] = speed[i];
        }

        Arrays.sort(zipped, (a,b) -> Double.compare(a[0],b[0]));
        Stack<Double> stack = new Stack();
        for (int i = zipped.length-1; i >= 0; i--){
            double curr = (target - zipped[i][0])/zipped[i][1];
            if (!stack.empty() && stack.peek() >= curr){
                curr = stack.pop();
            }
            stack.push(curr);
        }
        return stack.size();
    }
}
