class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        double[][] zipped = new double[position.length][2];

        for (int i = 0; i < position.length; i++){
            zipped[i][0] = position[i];
            zipped[i][1] = speed[i];
        }

        Arrays.sort(zipped, (a,b) -> Double.compare(b[0],a[0]));
        int fleets = 1;
        double prevTime = getTime(target, zipped[0][0], zipped[0][1]);
        for (int i = 1; i < position.length; i++){
            double curr = getTime(target, zipped[i][0], zipped[i][1]);
            if (prevTime < curr){
                fleets++;
                prevTime = curr;
            }
        }
        return fleets;
    }

    public double getTime(int target, double position, double speed){
        return (double)(target - position)/speed;
    }
}
