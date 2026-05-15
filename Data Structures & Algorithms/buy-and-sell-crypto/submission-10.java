class Solution {
    public int maxProfit(int[] prices) {
        int maxProf = 0;
        int minPrice = prices[0];

        for (int price: prices) {
            minPrice = Math.min(price, minPrice);
            maxProf = Math.max(price-minPrice, maxProf);
        }
        return maxProf;
    }
}
