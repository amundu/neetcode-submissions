class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int low = 1, high = Arrays.stream(piles).max().getAsInt();
        while(low < high){
            int mid = ((high-low)/2)+low;
            if (canEat(piles, h, mid)){
                high = mid;
            }else{
                low = mid + 1;
            }
        }
        return high;
    }

    private Boolean canEat(int[] piles, int h, int k){
        int total = 0;
        for (int i = 0; i < piles.length; i++){
            total += Math.ceil((double)piles[i]/k);
        }
        return total <= h;
    }
}
