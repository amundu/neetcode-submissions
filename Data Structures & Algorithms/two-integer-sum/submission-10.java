class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> remainders = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            int curr = target - nums[i];
            if (remainders.containsKey(curr)) {
                return new int[]{remainders.get(curr), i};
            }
            remainders.put(nums[i], i);
        }
        return new int[]{};
    }
}
